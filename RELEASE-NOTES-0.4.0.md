# Corrector ortografico aragonés 0.4.0

26 d’octubre de 2026. 21.098 dentradas Hunspell en UTF-8 (38 más que 0.3.0).

## Novedaz

- Revisión d’as reglas d’apostrofación y d’a autorización morfolochica d’os pronombres encliticos.
- Conservación d’a equivalencia entre apóstrofo dreito y tipografico.
- Revisión de lecturas nominals y verbals, conservando las formas con una lectura válida.
- Se conserva la segmentación por guión: l’acceptación de segmentos no certifica la corrección gramatical d’a cadena.

## Validación

Lo paquet de pruebas incluyiba comparanzas de 835 casos en Firefox y Enchant, sin diferencias con Hunspell nativo. Lo mantenedor ha confirmau que los paquets funcionan correctament en las aplicacions probadas. Las versions concretas d’as aplicacions no s’han rechistrau aquí.
Los paquets definitivos conservan exactament los AFF/DIC prebaus; s’actualiza la documentación y lo empaquetau.

## Limits

No ye un corrector gramatical ni una revisión exhaustiva d’o lexico. Veiga-se LECTURAS-Y-LIMITS.md.
La cifra de cobertura Common Voice de 88,66 % corresponde a 0.3.0 y no s’ha tornau a mesurar pa 0.4.0.

## Distribución

OXT pa LibreOffice; XPI separaus pa Firefox, Thunderbird y SeaMonkey; tar.gz pa Hunspell/Linux.
Los tres XPI son las copias publicadas d’os catalogos. Firefox conserva los fichers de firma de Mozilla; Thunderbird y SeaMonkey son identicos a los paquets puyaus. Los AFF/DIC son los definitivos. Lo README interno conserva la etiqueta «paquet de pruebas» d’a copia puyada; no s’ha modificau lo conteniu d’os XPI publicaus.

Licencia alternativa: MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later.
