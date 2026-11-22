# Corrector ortografico aragonés — Hunspell

Diccionario ortografico aragonés adaptau a la ortografía de l'Academia Aragonesa de la Lengua (AAL).

## Versión 1.1.0

- **52.001 dentradas DIC**, incluyindo radices ligadas que requieren afixación.
- Ampliación revisada d'adchectivos, adverbios, substantivos y verbos,
  contrastada con las fuentes históricas d'Apertium y DicAra.
- Flexión nominal y verbal y variants normativas expresament revisadas.
- Plurals, femeninos y alternancias d'acento mediante afixos compartius.
- Nombres propios con NOSUGGEST, identificadors estables FLAG num y
  conservación d'as revisions d'apostrofación, encliticos y sucherencias.

Consulta las [notas d'a versión](RELEASE-NOTES-1.1.0.md), la
[cobertura Common Voice](COBERTURA-COMMON-VOICE.md) y la
[procedencia](PROCEDENCIA.md).

## Descarga e instalación

Los paquez se distribuyen en [GitHub Releases](https://github.com/Juanpabl/hunspell-an/releases)
y en los catalogos de cada aplicación. Veiga-se [INSTALACION.md](INSTALACION.md).

- **LibreOffice:** emplegar lo `.oxt` d'esta versión. Lo diccionario incluyiu
  con una instalación de LibreOffice puede corresponder a una versión anterior.
  Asignar aragonés como luenga d'o texto y activar la revisión ortografica.
- **Firefox:** [Mozilla Add-ons](https://addons.mozilla.org/firefox/addon/corrector-ortografico-aragones/)
  u lo XPI firmau especifico de Firefox.
- **Thunderbird:** [Thunderbird Add-ons](https://addons.thunderbird.net/thunderbird/addon/corrector-ortografico-aragones/)
  u lo XPI especifico de Thunderbird.
- **SeaMonkey:** emplegar lo XPI clásico especifico, con install.rdf.
- **Hunspell:** conservar an_ES.aff y an_ES.dic chuntos, en UTF-8.

La versión disponible en cada canal puede diferir. Publicar en GitHub no
actualiza automaticament los catalogos ni lo diccionario incluyiu en LibreOffice.

## Validación y limits

La batería actual pasa **36.344 comprobacions** con Hunspell 1.7.2.
En Common Voice v25 reconoce **95,43 % por ocurrencias (82.817/86.783)**.
Lo método y los hashes se documentan en COBERTURA-COMMON-VOICE.md.

Lo corrector compreba parolas; no fa revisión gramatical. La cobertura no mide
precisión global ni certifica frases. La segmentación por guión u apóstrofo
puede influyir en una aplicación. Las versions minimas declaradas en los
manifests no significan que todas s'hayan prebau.

## Fichers y checksums

Los fuentes y la documentación son en este repositorio. Los instaladors se
publican como assets d'as releases; los scripts d'empaquetau son
build_release.py y mozilla/build_*.py.

SHA256SUMS.txt verifica los fuentes d'o repositorio. Los paquets tienen una
lista de sumas separada, calculada sobre los artefactos definitivos; pa Firefox,
sobre lo XPI firmau que se distribuya.

## Autors, licencia y colaboración

**Santiago Paricio:** autor orichinal.
**Juan Pablo Martínez:** colaborador dende 0.2 y responsable d'a adaptación AAL y revisions actuals.

Las incorporacions revisadas d'Apertium conservan los créditos de
**Jimmy O'Regan y Juan Pablo Martínez**. Se conservan tamién los avisos de
procedencia d'as atras fuentes y los créditos d'os colaboradors de Wikipedia
pa los nombres propios incorporaus.

Copyright (C) 2011 Santiago Paricio. Copyright (C) 2011–2026 Juan Pablo Martínez.

Trilicencia alternativa: **MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later**.
Textos completos en licenses/ y explicación en [LICENSE](LICENSE).

Incidencias y propostas: https://github.com/Juanpabl/hunspell-an/issues
Contacto: an.spellchecker@gmail.com

## English

Version **1.1.0** includes 52,001 dictionary entries, including bound stems,
with reviewed vocabulary and nominal and verbal inflection. It follows AAL
orthography and retains the apostrophe and enclitic-pronoun work of earlier
versions. Common Voice occurrence coverage is **95.43% (82,817/86,783)**.

This is a word-level dictionary, not a grammar checker. Application packages
are distributed through GitHub Releases and the respective add-on catalogs;
availability may differ between channels. Repository checksums cover source
files; release assets have separate checksums.

Available, at your option, under MPL 1.1, GPL 3.0 or later, or LGPL 3.0 or later.
Distributed WITHOUT WARRANTY under the selected license.
