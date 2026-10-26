"""Build and verify a classic SeaMonkey dictionary XPI from release sources."""
from pathlib import Path
import argparse
import hashlib
import zipfile
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('release_dir', type=Path)
parser.add_argument('output_dir', type=Path)
args = parser.parse_args()
source = args.release_dir.resolve()
output = args.output_dir.resolve()
output.mkdir(parents=True, exist_ok=True)
rdf = '''<?xml version="1.0" encoding="UTF-8"?>
<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
  <Description about="urn:mozilla:install-manifest">
    <em:id>hunspell-an-seamonkey@juanpabl.github.io</em:id>
    <em:version>0.4.0</em:version>
    <em:type>64</em:type>
    <em:unpack>true</em:unpack>
    <em:name>Corrector ortografico aragonés — SeaMonkey</em:name>
    <em:description>Diccionario ortografico aragonés adaptau a la ortografía AAL.</em:description>
    <em:creator>Santiago Paricio y Juan Pablo Martínez</em:creator>
    <em:homepageURL>https://github.com/Juanpabl/hunspell-an</em:homepageURL>
    <em:targetApplication>
      <Description>
        <em:id>{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}</em:id>
        <em:minVersion>2.53</em:minVersion>
        <em:maxVersion>2.53.*</em:maxVersion>
      </Description>
    </em:targetApplication>
  </Description>
</RDF>
'''.encode('utf-8')
payload = {
    'install.rdf': rdf,
    'dictionaries/an.dic': (source / 'an_ES.dic').read_bytes(),
    'dictionaries/an.aff': (source / 'an_ES.aff').read_bytes(),
    'README_an_ES.txt': (source / 'README_an_ES.txt').read_bytes(),
}
for f in (source / 'licenses').glob('*.txt'):
    payload['licenses/' + f.name] = f.read_bytes()
xpi = output / 'corrector-ortografico-aragones.0.4.0-seamonkey.xpi'
with zipfile.ZipFile(xpi, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, data in sorted(payload.items()):
        info = zipfile.ZipInfo(name, date_time=(2026, 10, 13, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, data)
with zipfile.ZipFile(xpi) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == set(payload)
    root = ET.fromstring(z.read('install.rdf'))
    ns = {'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'em': 'http://www.mozilla.org/2004/em-rdf#'}
    manifest = root.find('rdf:Description', ns)
    assert manifest.find('em:type', ns).text == '64'
    assert manifest.find('em:id', ns).text == 'hunspell-an-seamonkey@juanpabl.github.io'
    assert manifest.find('em:version', ns).text == '0.4.0'
    assert len(manifest.findall('em:targetApplication', ns)) == 1
    assert manifest.find('em:targetApplication/rdf:Description/em:id', ns).text == '{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}'
    for name, data in payload.items():
        assert z.read(name) == data
    assert 'manifest.json' not in z.namelist()
metadata = output / 'mozilla' / 'seamonkey'
metadata.mkdir(parents=True, exist_ok=True)
(metadata / 'install.rdf').write_bytes(rdf)
(output / 'mozilla' / 'build_seamonkey.py').write_bytes(Path(__file__).read_bytes())
print('Verified ZIP, RDF, SeaMonkey-only target and exact dictionary content.')
print(xpi.name, hashlib.sha256(xpi.read_bytes()).hexdigest())
