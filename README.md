# Corrector ortografico aragonés — Hunspell

Diccionario ortografico aragonés adaptau a la ortografía de l’Academia Aragonesa de la Lengua (AAL).

## Estau actual

**La branca de desenvolvimiento contiene la candidata 1.0.0. Encara no ye una release publicada.**
La zaguera release publicada ye [0.4.0](https://github.com/Juanpabl/hunspell-an/releases/tag/v0.4.0). Las descargas d’os catalogos pueden corresponder a ixa versión; este commit no publica una actualización en Mozilla, Thunderbird ni LibreOffice.

## Candidata 1.0.0

- 40.880 dentradas DIC, incluyindo radices ligadas.
- 16.868 reglas d’afixos y 108 reglas REP, seguntes los recuentos d’a candidata.
- Ampliación revisada d’o lexico y paradigmas procedentes d’Apertium.
- Flexión regular e irregular y variants dialectals revisadas.
- Nombres propios nuevos con NOSUGGEST, sin promover-los en las sucherencias.
- Identificadors numericos d’afixos (`FLAG num`).
- Conservación d’as regresions d’apostrofación y encliticos d’a 0.4.0.

Consulta cobertura Common Voice (COBERTURA-COMMON-VOICE.md).

## Validación y limits

La documentación d’a candidata rechistra 306.007 casos normativos sin discrepancias y una cobertura de Common Voice de 92,81 % por ocurrencias (80.546/86.783), con Hunspell 1.7.2. Estes resultaus proceden d’o treballo previo; este commit no los torna a executar. La cobertura no mide precisión ni certifica frases.

Las prebas d’interficie de 0.4.0 no certifican automaticament 1.0.0. Falta validar esta candidata exacta en las aplicacions antes de publicar los paquets definitivos.
Lo corrector compreba parolas; no fa revisión gramatical. La segmentación por guión u apóstrofo puede influyir en lo resultau d’una aplicación.

## Instalación

Pa uso habitual, emplegar los paquets de [la release 0.4.0](https://github.com/Juanpabl/hunspell-an/releases/tag/v0.4.0).
Pa probar los fuentes 1.0.0 con Hunspell, seguir [INSTALACION.md](INSTALACION.md). Conservar los fichers `an_ES.aff` y `an_ES.dic` chuntos, en UTF-8. Lo OXT candidato se prepara y preba localment; no s’incluye como asset d’una release en este commit.

## Autors, licencia y colaboración

Santiago Paricio: autor orichinal. Juan Pablo Martínez: colaborador dende 0.2 y responsable d’a adaptación AAL y revisions actuals.

Copyright (C) 2011 Santiago Paricio. Copyright (C) 2011–2026 Juan Pablo Martínez.

Trilicencia alternativa: **MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later**. Puez triar una d’as tres; textos completos en `licenses/` y explicación en [LICENSE](LICENSE).

Incidencias y propuestas: https://github.com/Juanpabl/hunspell-an/issues
Contacto: an.spellchecker@gmail.com

## English

The development branch contains the **1.0.0 release candidate**, not a published release. The latest published release remains 0.4.0. Application testing of this exact candidate is still required. This is a word-level Hunspell dictionary, not a grammar checker.
