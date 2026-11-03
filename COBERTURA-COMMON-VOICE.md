# Cobertura en Common Voice — 1.0.0

**92,81 %** d'ocurrencias reconocidas (80,546 de
86,783). Quedan 6,237 ocurrencias desconocidas,
4,192 formas distintas.

Corpus UTF-8: frases_para_hunspell.txt.
SHA-256: `c1c468650fd3fa907f9d00605fd3864043dc61fa2ae03606bfbd363d5db7ff5f`.
Motor: Hunspell 1.7.2, mesmos texto, opciones y segmentación: `-i UTF-8
--no-default-personal -d ./an_ES -G` y `-l`. Denominador: reconocidas +
desconocidas emitidas por lo motor; las marcas y numeros omitius no cuentan.
Los apostrofos pueden segmentar-se; no ye una medida por frase completa.

Frente a la instantania anterior a las zagueras series 
No comparar porcentaches de corpus u segmentacions diferents como si fuesen
la mesma mesura. Las desconocidas no son automaticament errors y la cobertura
no certifica precisión. Listau por frecuencia en o reposte de treballo:
`desarrollo/fase1/desconocidas-por-frecuencia.tsv`.

Par exacto:
- DIC: `733dce3919b72db3e844228733d14936ebebde5c59f6a5b49e73d47390dde69d`
- AFF: `7b1763cb88b5e2dda4d8f57780541225f0b08a6c6867b2d681183323bea87b61`
