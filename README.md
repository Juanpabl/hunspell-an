# Corrector ortografico aragonés — Hunspell

Diccionario ortografico aragonés adaptau a la **ortografía de l’Academia Aragonesa de la Lengua (AAL)**, pa aplicaciones compatibles con Hunspell.

**Versión 0.3.0 · 13 d’octubre de 2026 · Idioma: aragonés (`an-ES`).**

Incluye **21.060 dentradas** y reglas d’afixación que cheneran formas flexionadas y derivadas. Lo paquet d’esta versión ha estau prebau en LibreOffice.

## Descarga e instalación

Los paquets de distribución se publican en la sección **Releases** d’este repositorio.

### LibreOffice

1. Descarga `corrector-ortografico-aragones.0.3.0.oxt` dende **Releases**.
2. Ubre lo chestor d’extensions de LibreOffice y tría **Anyadir**.
3. Selecciona lo fichero `.oxt`, completa la instalación y reinicia LibreOffice.
4. Asigna l’idioma **aragonés** a lo texto y activa la revisión ortografica.

Si tiens unatro diccionario aragonés instalau, desactiva-lo u retira-lo pa evitar que los dos interviengan en la comprebación.

### Hunspell y atras aplicaciones

Los fichers `an_ES.aff` y `an_ES.dic` son codificaus en UTF-8. Han d’estar chuntos y conservar lo mesmo nombre base.

La instalación y configuración penden de cada aplicación. Lo paquet `.oxt` ye pa LibreOffice; Firefox y Thunderbird requieren un paquet propio.

## Ortografía y alcanz

La versión 0.3.0 adapta lo corrector a la [Ortografía de l’Aragonés de l’Academia Aragonesa de la Lengua](https://academiaaragonesadelalengua.org/sites/default/files/ficheros-pdf/ortografia-de-laragones_web_an.pdf).

Lo corrector **compreba parolas, sin fer garra revisión gramatical de frases**. La cobertura encara ye incompleta: una parola marcada puede estar correcta y una parola acceptada puede estar mal emplegada en lo suyo contexto.

La cobertura en lo corpus aragonés de **Common Voice v25** ye de **88,66 % per ocurrencias**. Esta cifra describe la cobertura en ixe corpus, no la precisión global d’o corrector.

## Conteniu d’a distribución

- `corrector-ortografico-aragones.0.3.0.oxt`: extensión pa LibreOffice.
- `an_ES.dic` y `an_ES.aff`: fichers Hunspell en UTF-8.
- `INSTALACION.md`: instrucciones d’instalación y actualización.
- `RELEASE-NOTES-0.3.0.md`: novedaz, validación y limitacions.
- `COBERTURA-COMMON-VOICE.md`: cobertura d’o corpus de referencia.
- `licenses/`: textos completos d’as licencias.
- `SHA256SUMS.txt`: sumas de comprebación d’os fichers distribuius.

## Incidencias y colaboración

Las sucherencias de vocabulario y las correccions son bienvenidas. Puedes ubrir una **Issue** en este repositorio u escribir a **an.spellchecker@gmail.com**, indicando:

- La parola y una frase de contexto.
- Lo resultau actual y lo resultau asperau.
- La versión d’o corrector y de l’aplicación emplegada.
- Una referencia lingüistica, si en tiens.

## Autors y creditos

- **Santiago Paricio**: autor orichinal.
- **Juan Pablo Martínez**: colaborador dende la versión 0.2; responsable de l’adaptación a la ortografía AAL, revisión lingüistica y ampliacions de 0.3.0.

La versión 0.2 emplegó corpus libres, como Wikipedia en aragonés, y listas de parolas procedentes de diccionarios d’Apertium. La versión 0.3 ha emplegau lo corpus de Common Voice v25.

Copyright (C) 2011 Santiago Paricio <sparicio@gmail.com>.

Copyright (C) 2011–2026 Juan Pablo Martínez <jpmart@unizar.es>.

## Licencia

Lo listau `.dic` y lo fichero d’afixos `.aff` se distribuyen baixo una **trilicencia alternativa**. Puedes triar entre:

- Mozilla Public License 1.1.
- GNU General Public License 3.0 u posterior.
- GNU Lesser General Public License 3.0 u posterior.

No ye menister cumplir las tres simultaniament. Se distribuyen sin garantía, seguntes los termens d’a licencia triada. Los textos completos s’incluyen en `licenses/`.

**Identificador SPDX:** `MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later`.

## English

Aragonese Hunspell spelling dictionary following the orthography of the Academia Aragonesa de la Lengua (AAL).

Version 0.3.0 includes 21,060 dictionary entries, affix rules and a tested LibreOffice extension. This is a word-level spellchecker, not a grammar checker.

The dictionary and affix files are available, at your option, under MPL 1.1, GPL 3.0 or later, or LGPL 3.0 or later. Distributed **WITHOUT WARRANTY** under the terms of the selected license. Full license texts are included in `licenses/`.
