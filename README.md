# Corrector ortografico aragonés — Hunspell

Diccionario ortografico aragonés adaptau a la **ortografía de l’Academia Aragonesa de la Lengua (AAL)**, pa aplicacions compatibles con Hunspell.

**Versión 0.4.0 · 26 d’octubre de 2026 · Idioma: aragonés (`an-ES`).**

Incluye **21.098 dentradas** y reglas d’afixación que cheneran formas flexionadas y derivadas. Lo paquet d’esta versión ha estau prebau en LibreOffice.

La 0.4.0 revisa apostrofacions y encliticos. Consulta las [novedaz](RELEASE-NOTES-0.4.0.md). Los enlaces a v0.4.0 funcionarán quan se publique la release.

## Descarga e instalación

Descarga la versión 0.4.0 en [Releases](https://github.com/Juanpabl/hunspell-an/releases/tag/v0.4.0).

- [Firefox: instalar dende Mozilla Add-ons](https://addons.mozilla.org/firefox/addon/corrector-ortografico-aragones/).
- [Thunderbird: instalar dende Thunderbird Add-ons](https://addons.thunderbird.net/thunderbird/addon/corrector-ortografico-aragones/).
- LibreOffice: descargar lo `.oxt` d’a Release.

Los tres XPI son las copias publicadas d’os catalogos. Firefox conserva los fichers de firma de Mozilla; Thunderbird y SeaMonkey son identicos a los paquets puyaus. Los AFF/DIC son los definitivos. Lo README interno conserva la etiqueta «paquet de pruebas» d’a copia puyada; no s’ha modificau lo conteniu d’os XPI publicaus.

### LibreOffice

1. Descarga `corrector-ortografico-aragones.0.4.0.oxt` dende **Releases**.
2. Ubre lo chestor d’extensions de LibreOffice y tría **Anyadir**.
3. Selecciona lo fichero `.oxt`, completa la instalación y reinicia LibreOffice.
4. Asigna l’idioma **aragonés** a lo texto y activa la revisión ortografica.

Si tiens unatro diccionario aragonés instalau, desactiva-lo u retira-lo pa evitar que los dos interviengan en la comprebación.

### Linux / Hunspell

En Debian y Ubuntu:

```sh
sudo apt install hunspell hunspell-an
```

Lo diccionario empaquetau puede ser anterior a 0.4.0. Pa emplegar esta entrega,
descarga [hunspell-an-0.4.0.tar.gz](https://github.com/Juanpabl/hunspell-an/releases/download/v0.4.0/hunspell-an-0.4.0.tar.gz)
y sigue las [instruccions d'instalación manual en Linux](INSTALACION-LINUX.md).
Lo paquet incluye lo par `.aff`/`.dic`, documentación y licencias, sin precisar
los paquets d'extensions de Firefox u LibreOffice.

### Hunspell y atras aplicacions

Los fichers `an_ES.aff` y `an_ES.dic` son codificaus en UTF-8. Han d’estar chuntos y conservar lo mesmo nombre base.

La instalación y configuración penden de cada aplicación. Lo paquet `.oxt` ye pa LibreOffice; cada `.xpi` ye pa la aplicación indicada en lo suyo nombre. Consulta [Instalación pa Mozilla](INSTALACION-MOZILLA.md).

## Documentación

- [Instalación en LibreOffice y Hunspell](INSTALACION.md)
- [Instalación en Linux y descarga manual de 0.4.0](INSTALACION-LINUX.md)
- [Instalación en Firefox y Thunderbird](INSTALACION-MOZILLA.md)
- [Novedaz de 0.4.0](RELEASE-NOTES-0.4.0.md)
- [Cobertura en Common Voice](COBERTURA-COMMON-VOICE.md)

## Ortografía y alcanz

Dende la versión 0.3.0, lo corrector s’adapta a la [Ortografía de l’Aragonés de l’Academia Aragonesa de la Lengua](https://academiaaragonesadelalengua.org/sites/default/files/ficheros-pdf/ortografia-de-laragones_web_an.pdf).

Lo corrector **compreba parolas, sin fer garra revisión gramatical de frases**. La cobertura encara ye incompleta: una parola marcada puede estar correcta y una parola acceptada puede estar mal emplegada en lo suyo contexto.

La cobertura mesurada pa **0.3.0** en lo corpus aragonés de **Common Voice v25** fue de **88,66 % per ocurrencias**; no s’ha tornau a mesurar pa 0.4.0. Esta cifra describe la cobertura en ixe corpus, no la precisión global d’o corrector.

## Conteniu d’a distribución

- `corrector-ortografico-aragones.0.4.0.oxt`: extensión pa LibreOffice.
- `an_ES.dic` y `an_ES.aff`: fichers Hunspell en UTF-8.
- `hunspell-an-0.4.0.tar.gz`: diccionario, documentación y licencias pa Hunspell.
- `LICENSE`: explicación d'a trilicencia alternativa.
- `INSTALACION.md`: instrucciones d’instalación y actualización.
- `RELEASE-NOTES-0.4.0.md`: novedaz, validación y limitacions.
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
- **Juan Pablo Martínez**: colaborador dende la versión 0.2; responsable de l’adaptación a la ortografía AAL, revisión lingüistica y ampliacions de 0.4.0.

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

Version 0.4.0 includes 21,098 dictionary entries, affix rules and a tested LibreOffice extension. This is a word-level spellchecker, not a grammar checker.

The dictionary and affix files are available, at your option, under MPL 1.1, GPL 3.0 or later, or LGPL 3.0 or later. Distributed **WITHOUT WARRANTY** under the terms of the selected license. Full license texts are included in `licenses/`.

