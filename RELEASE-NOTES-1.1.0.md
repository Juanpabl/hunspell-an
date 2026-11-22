# Corrector ortografico aragonés 1.1.0

22 de noviembre de 2026.

Esta versión amplía y revisa lo lexico y la flexión d'a 1.0.0, mantendo la
ortografía de l'Academia Aragonesa de la Lengua y los criterios lingüisticos
aprebaus.

- Revisión e incorporación d'adchectivos, adverbios, substantivos y verbos
  d'as fuentes históricas d'Apertium, contrastadas con DicAra.
- Flexión nominal y verbal regular e irregular, participios y variants
  normativas expresament revisadas. Las grafías refusadas no s'importan
  automaticament d'as lecturas toleradas por Apertium.
- Ampliación d'as series verbals admitidas y reglas especificas pa alternancias
  de radical y compuestos de fer con acentuación propia.
- Consolidación de plurals, femeninos y atras flexions sencillas mediante
  afixos, incluyindo cambios d'acento; reducción de dentradas redundants.
- Apostrofación productiva mediante reglas, evitando dentradas literals
  innecesarias y l'apostrofación de l'articlo singular debant de plurals.
- Se conservan FLAG num, los identificadors d'afixos y las revisions
  d'apostrofación, encliticos y sucherencias d'as versions anteriors.

## Dimensión y cobertura

Lo DIC pasa de **40.880 a 52.001 dentradas**, un aumento neto de 11.121.
Las dentradas incluyen radices ligadas y no equivalen a lemas u parolas distintas.

En lo mesmo corpus Common Voice v25 se reconoixen **82.817 de 86.783
ocurrencias: 95,43 %**, frente a 80.546/86.783 (92,81 %) en 1.0.0.
Son 2.271 ocurrencias reconocidas más y un aumento de 2,62 puntos porcentuals.
Veiga-se COBERTURA-COMMON-VOICE.md pa lo método y los hashes exactos.

## Comprebación y limits

La batería actual comprende **36.344 comprobacions**, sin discrepancias,
con Hunspell nativo 1.7.2. Ye una batería de parolas y autorización d'afixos;
no ye lo mesmo recuento ni l'alcanz d'os 306.007 casos citados pa 1.0.0.

La cobertura mide reconocimiento, no precisión global ni corrección gramatical.
Las pruebas d'instalación y actualización en las aplicacions se rechistran
per separau. No s'atribuyen pruebas de versions anteriors a los nuevos paquets.

Se conservan los créditos y la trilicencia alternativa
MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later.
