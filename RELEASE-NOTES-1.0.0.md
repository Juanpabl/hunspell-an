# Corrector aragonés 1.0.0

Esta versión amplía lo lexico y la flexión revisada d'a 0.4.0. Lo nombre
provisional d'este treballo yera 0.5.0; la candidata final pasa a **1.0.0**.

* Incorporación revisada de lemas d'Apertium por categorías y paradigmas: parolas
invariables, numerals, adchectivos, substantivos, nombres propios y verbos.
* Flexión verbal regular e irregular y variants dialectals expresament
aprebadas; no se trasladan indiscriminadament las formas nomás analisables.
* Nombres propios nuevos con NOSUGGEST: se reconoixen sin promover-los como
sucherencias pa errors d'atras parolas.
* Sucherencias pa grafías anteriors y terminacions: las REP no autorizan
las grafías refusadas ni sustituyen una conversión ortografica completa.
* FLAG num con identificadors estables y catalogo documentau, pa facilitar
la edición manual. No s'ha aplicau una refactorización recursiva general.
* Conservadas las regresions d'apostrofacions y encliticos de 0.4.0.

## 

## Comprebación

306,007 casos normativos verificaús por alcance, sin
discrepancias. Corpus Common Voice: **92,81 %** por ocurrencias;
80,546/86,783 reconocidas.
La cobertura no mide precisión ni certifica todas las frases.

Lo par exacto s'ha comprebau con Hunspell 1.7.2. 

Se conservan los créditos y la trilicencia alternativa
MPL 1.1 / GPL 3+ / LGPL 3+; no cal cumplir las tres simultaniament.

