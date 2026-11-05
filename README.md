# Corrector ortografico aragonés — Hunspell

Diccionario ortografico aragonés adaptau a la ortografía de l’Academia Aragonesa de la Lengua (AAL).

## Versión 1.0.0

- **40.880 dentradas DIC**, incluyindo radices ligadas que requieren afixación.
- Ampliación revisada d’o lexico y paradigmas procedentes d’Apertium.
- Flexión nominal y verbal regular e irregular y variants dialectals revisadas.
- Nombres propios nuevos con `NOSUGGEST`: se reconoixen sin proponer-los como sucherencias de corrección.
- Milloras en las sucherencias pa grafías anteriors y terminacions.
- Identificadors numericos d’afixos (`FLAG num`).
- Conservación d’as revisions d’apostrofación y encliticos d’a 0.4.0.

Consulta las [notas d’a versión](RELEASE-NOTES-1.0.0.md) y la [cobertura Common Voice](COBERTURA-COMMON-VOICE.md).

## Descarga e instalación

Los paquets definitivos s’ofrirán en [la release v1.0.0](https://github.com/Juanpabl/hunspell-an/releases/tag/v1.0.0) quan se publique. Mientras tanto, las versions ya publicadas son en [Releases](https://github.com/Juanpabl/hunspell-an/releases).

- **LibreOffice:** instalar lo `.oxt` dende lo chestor d’extensions y asignar aragonés a lo texto.
- **Firefox:** instalar dende [Mozilla Add-ons](https://addons.mozilla.org/firefox/addon/corrector-ortografico-aragones/). Pa instalación manual, emplegar lo XPI firmau de Firefox.
- **Thunderbird:** instalar dende [Thunderbird Add-ons](https://addons.thunderbird.net/thunderbird/addon/corrector-ortografico-aragones/), u emplegar lo suyo XPI especifico.
- **SeaMonkey:** emplegar lo XPI clásico especifico, quan siga disponible. No ye lo mesmo paquet que lo de Thunderbird.
- **Hunspell:** conservar `an_ES.aff` y `an_ES.dic` chuntos, en UTF-8. Veiga-se [INSTALACION.md](INSTALACION.md).

La versión disponible en cada catalogo puede diferir; comprobar-la antes de instalar. La publicación en GitHub no actualiza automaticament los catalogos ni lo diccionario incluyiu en LibreOffice.

## Validación y limits

La documentación de 1.0.0 rechistra **306.007 casos normativos sin discrepancias en l’alcanz evaluau**, con Hunspell 1.7.2, y **92,81 % de cobertura por ocurrencias** en Common Voice v25 (80.546/86.783). La cobertura no mide precisión global ni certifica frases.

Lo corrector compreba parolas; no fa revisión gramatical. La cobertura lexica y morfolochica encara ye incompleta. La segmentación por guión u apóstrofo puede influyir en lo resultau d’una aplicación. Las versions minimas declaradas en los manifests no significan que todas s’hayan prebau.

## Fichers y checksums

Los fuentes y documentación son en este repositorio; los instaladors se distribuyen como assets d’as releases. `mozilla/` contiene los manifests y scripts d’empaquetau.

`SHA256SUMS.txt` d’a raíz verifica los fichers d’o repositorio. Las sumas d’os paquets distribuius han d’acompanyar los assets d’a release y se calculan sobre los paquets definitivos, incluyindo la copia firmada de Firefox.

## Autors, licencia y colaboración

**Santiago Paricio:** autor orichinal.
**Juan Pablo Martínez:** colaborador dende 0.2 y responsable d’a adaptación AAL y revisions actuals.

La incorporación revisada d’Apertium conserva los créditos de **Jimmy O’Regan y Juan Pablo Martínez**. Se conservan tamién los avisos de procedencia d’as atras fuentes y los créditos d’os colaboradors de Wikipedia pa los nombres propios incorporaus.

Copyright (C) 2011 Santiago Paricio. Copyright (C) 2011–2026 Juan Pablo Martínez.

Trilicencia alternativa: **MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later**. Puez triar una d’as tres; no cal cumplir-las simultaniament. Textos completos en `licenses/` y explicación en [LICENSE](LICENSE).

Incidencias y propostas: https://github.com/Juanpabl/hunspell-an/issues
Contacto: an.spellchecker@gmail.com

## English

Version **1.0.0** includes 40,880 dictionary entries, including bound stems, expanded vocabulary and reviewed nominal and verbal paradigms. It follows AAL orthography and retains the apostrophe and enclitic-pronoun improvements of 0.4.0.

This is a word-level Hunspell dictionary, not a grammar checker. Coverage remains incomplete. Application packages are distributed through GitHub Releases and the respective add-on catalogs; availability may differ between channels. The repository checksum file covers source files, not release assets.

Available, at your option, under MPL 1.1, GPL 3.0 or later, or LGPL 3.0 or later. Distributed WITHOUT WARRANTY under the selected license.
