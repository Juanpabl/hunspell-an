import argparse
import csv
import ctypes
import ctypes.util
import hashlib
import json
from pathlib import Path
import tempfile


class Engine:
    def __init__(self, base, library):
        self.lib = ctypes.CDLL(library)
        self.lib.Hunspell_create.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.Hunspell_create.restype = ctypes.c_void_p
        self.lib.Hunspell_spell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lib.Hunspell_spell.restype = ctypes.c_int
        self.lib.Hunspell_destroy.argtypes = [ctypes.c_void_p]
        self.lib.Hunspell_get_dic_encoding.argtypes = [ctypes.c_void_p]
        self.lib.Hunspell_get_dic_encoding.restype = ctypes.c_char_p
        self.handle = self.lib.Hunspell_create(str(base.with_suffix('.aff')).encode(),
                                               str(base.with_suffix('.dic')).encode())
        if not self.handle:
            raise RuntimeError('Cannot load dictionary: ' + str(base))
        self.encoding = self.lib.Hunspell_get_dic_encoding(self.handle).decode('ascii')

    def spell(self, word):
        return bool(self.lib.Hunspell_spell(self.handle, word.encode(self.encoding)))

    def close(self):
        self.lib.Hunspell_destroy(self.handle)


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Check reviewed words with native Hunspell.")
    parser.add_argument('--dictionary', type=Path, default=here.parent / 'an_ES')
    parser.add_argument('--cases', type=Path, default=here / 'casos-revision-lexica.tsv')
    parser.add_argument('--library')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    library = args.library or ctypes.util.find_library('hunspell-1.7') or ctypes.util.find_library('hunspell')
    if not library:
        parser.error('Native Hunspell library not found; install it or pass --library')
    base = args.dictionary.resolve()
    with args.cases.open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    assert rows and all(r['criterio'] in ('ACEPTAR', 'RECHAZAR') and
                        r['alcance'] in ('PALABRA', 'AFIJACION') for r in rows)
    assert len({(r['forma'], r['alcance']) for r in rows}) == len(rows)
    aff = base.with_suffix('.aff').read_text(encoding='utf-8')
    assert not any(l.split('#', 1)[0].strip().startswith('BREAK ') for l in aff.splitlines())
    failures = []
    checks = 0
    with tempfile.TemporaryDirectory(prefix='hunspell-an-test-') as folder:
        isolated = Path(folder) / 'an_ES'
        isolated.with_suffix('.dic').write_bytes(base.with_suffix('.dic').read_bytes())
        isolated.with_suffix('.aff').write_text(aff + '\nBREAK 0\n', encoding='utf-8')
        engines = {'PALABRA': Engine(base, library), 'AFIJACION': Engine(isolated, library)}
        try:
            for row in rows:
                for word in sorted({row['forma'], row['forma'].replace("'", '’')}):
                    actual = engines[row['alcance']].spell(word)
                    expected = row['criterio'] == 'ACEPTAR'
                    checks += 1
                    if actual != expected:
                        failures.append({**row, 'forma': word, 'accepted': actual})
        finally:
            for engine in engines.values():
                engine.close()
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    report = {'status': 'FAIL' if failures else 'PASS', 'native_library': library,
              'case_rows': len(rows), 'checks': checks, 'failures': failures,
              'dictionary_sha256': {ext: sha(base.with_suffix(ext)) for ext in ('.dic', '.aff')},
              'cases_sha256': sha(args.cases),
              'scope': 'Normal segmentation for PALABRA; temporary BREAK 0 for AFIJACION. Word-level regression tests, not grammatical or corpus precision.'}
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
