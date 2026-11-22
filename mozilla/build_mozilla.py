"""Build deterministic Firefox and Thunderbird dictionary packages."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('release_dir', type=Path)
parser.add_argument('output_dir', type=Path)
args = parser.parse_args()
source = args.release_dir.resolve()
output = args.output_dir.resolve()
output.mkdir(parents=True, exist_ok=True)

for app in ['firefox', 'thunderbird']:
    manifest = json.loads((source / 'mozilla' / app / 'manifest.json').read_text(encoding='utf-8'))
    assert manifest['version'] == '1.1.0'
    assert manifest['browser_specific_settings']['gecko']['id'] == 'an-ES@dictionaries.addons.mozilla.org'
    payload = {
        'manifest.json': (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8'),
        'dictionaries/an_ES.aff': (source / 'an_ES.aff').read_bytes(),
        'dictionaries/an_ES.dic': (source / 'an_ES.dic').read_bytes(),
        'README_an_ES.txt': (source / 'README_an_ES.txt').read_bytes().replace(b'PROCEDENCIA.md', b'PROCEDENCIA.txt'),
        'PROCEDENCIA.txt': (source / 'PROCEDENCIA.md').read_bytes(),
    }
    for license_file in (source / 'licenses').glob('*.txt'):
        payload['licenses/' + license_file.name] = license_file.read_bytes()
    xpi = output / f'corrector-ortografico-aragones.1.1.0-{app}-unsigned.xpi'
    with zipfile.ZipFile(xpi, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 22, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    manifest_dir = output / 'mozilla' / app
    manifest_dir.mkdir(parents=True, exist_ok=True)
    (manifest_dir / 'manifest.json').write_bytes(payload['manifest.json'])
    with zipfile.ZipFile(xpi) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(payload)
        for name, data in payload.items():
            assert archive.read(name) == data
        parsed = json.loads(archive.read('manifest.json'))
        assert parsed['browser_specific_settings']['gecko']['id'] == 'an-ES@dictionaries.addons.mozilla.org'
        assert 'dictionaries/an_ES.dic' in archive.namelist()
        assert 'dictionaries/an_ES.aff' in archive.namelist()
        assert 'permissions' not in parsed and 'background' not in parsed
    print(xpi.name, hashlib.sha256(xpi.read_bytes()).hexdigest())

(output / 'mozilla' / 'build_mozilla.py').write_bytes(Path(__file__).read_bytes())
