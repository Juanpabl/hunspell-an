"""Build OXT, source archive and application XPIs from reviewed release files."""
from pathlib import Path
import argparse
import gzip
import hashlib
import io
import subprocess
import sys
import tarfile
import xml.etree.ElementTree as ET
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('release_dir', type=Path)
parser.add_argument('output_dir', type=Path)
args = parser.parse_args()
source = args.release_dir.resolve()
output = args.output_dir.resolve()
if output == source or source in output.parents:
    parser.error('Use an output directory outside the release sources.')
root = ET.parse(source / 'description.xml').getroot()
ns = {'d': 'http://openoffice.org/extensions/description/2006'}
version = root.find('d:version', ns).get('value')
assert version == '1.1.0'
assert root.find('d:identifier', ns).get('value') == 'org.aragones.hunspell.aal'
# Reject stale or changed sources before making an installer.
for line in (source / 'SHA256SUMS.txt').read_text().splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((source / name).read_bytes()).hexdigest() == expected, name
output.mkdir(parents=True, exist_ok=True)
stamp = (2026, 11, 22, 0, 0, 0)
packages = []
notes = 'RELEASE-NOTES-' + version + '.md'
common = ['an_ES.aff', 'an_ES.dic', 'README_an_ES.txt', 'PROCEDENCIA.md',
          'LICENSE', notes, 'COBERTURA-COMMON-VOICE.md', 'README.md',
          'INSTALACION.md', 'INSTALACION-LINUX.md', 'INSTALACION-MOZILLA.md',
          'INSTALACION-SEAMONKEY.md', 'LECTURAS-Y-LIMITS.md']
payload = {name: (source / name).read_bytes() for name in common}
for file in sorted((source / 'licenses').glob('*.txt')):
    payload['licenses/' + file.name] = file.read_bytes()
for name in ['description.xml', 'dictionaries.xcu', 'META-INF/manifest.xml']:
    payload[name] = (source / name).read_bytes()
oxt = output / ('corrector-ortografico-aragones.' + version + '.oxt')
with zipfile.ZipFile(oxt, 'w', zipfile.ZIP_DEFLATED) as archive:
    for name, data in sorted(payload.items()):
        info = zipfile.ZipInfo(name, date_time=stamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, data)
with zipfile.ZipFile(oxt) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == set(payload)
    for name, data in payload.items():
        assert archive.read(name) == data
packages.append(oxt)

# The source archive includes the reviewed scripts, tests and source checksums.
# No generated installers, signing files or repository metadata are included.
names = [line.split('  ', 1)[1] for line in
         (source / 'SHA256SUMS.txt').read_text().splitlines()]
names.append('SHA256SUMS.txt')
tar_path = output / ('hunspell-an-' + version + '.tar.gz')
with tar_path.open('wb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as compressed:
    with tarfile.open(fileobj=compressed, mode='w') as archive:
        for name in sorted(names):
            data = (source / name).read_bytes()
            info = tarfile.TarInfo('hunspell-an-' + version + '/' + name)
            info.size = len(data)
            info.mode = 0o644
            info.mtime = 1795305600  # 2026-11-22 00:00:00 UTC
            archive.addfile(info, io.BytesIO(data))
with tarfile.open(tar_path, 'r:gz') as archive:
    for name in names:
        assert archive.extractfile('hunspell-an-' + version + '/' + name).read() == (source / name).read_bytes()
packages.append(tar_path)
for builder in ['build_mozilla.py', 'build_seamonkey.py']:
    subprocess.run([sys.executable, str(source / 'mozilla' / builder),
                    str(source), str(output)], check=True)
packages += [output / ('corrector-ortografico-aragones.' + version + '-' + app + '-unsigned.xpi')
             for app in ['firefox', 'thunderbird']]
packages.append(output / ('corrector-ortografico-aragones.' + version + '-seamonkey.xpi'))
sums = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n'
               for p in sorted(packages))
(output / 'SHA256SUMS-PAQUETS.txt').write_text(sums)
print(sums, end='')
print('Firefox is unsigned. Recompute final asset checksums after signing.')
