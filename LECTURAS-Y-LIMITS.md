# Lecturas y limits d'a 1.1.0

Lo corrector reconoce parolas y formas flexionadas; no fa análisis sintactico
ni revisión gramatical. Una cadena s'accepta si tiene beluna lectura válida,
anque en un contexto concreto pueda estar incorrecta.

Se conservan las revisions d'apostrofación y encliticos d'a 0.4.0. Lo guión y
los apostrofos pueden segmentar-se de maneras diferents seguntes l'aplicación.
Cal distinguir la autorización d'afixos d'Hunspell d'a tokenización de la
interficie. No se puede deducir d'una prueba aislada que toda frase ye correcta.

Las incorporacions d'Apertium y las fuentes históricas se revisan por categorías
y paradigmas. Las variants normativas pueden estar en Hunspell; las grafías
no normativas toleradas nomás pa l'analís en Apertium no s'importan por defecto.
DicAra s'emplega como referencia lexical, no como incorporación indiscriminada.

La batería actual contiene comprobacions positivas y negativas de parolas y
autorización d'afixos. Sus 36.344 comprobacions no tienen lo mesmo alcance que
los recuentos históricos d'atras versions; no se suman ni se comparan como si
fuesen una mesma batería. Los resultados exactos son en tests/VERIFICACION.json.

La cobertura Common Voice mide reconocimiento por ocurrencias emitidas por
Hunspell, no precisión ni corrección de frases. Las desconocidas pueden estar
parolas correctas que faltan, errors, nombres propios u problemas de segmentación.
Veiga-se COBERTURA-COMMON-VOICE.md pa los denominadors y las sumas del par.

La instalación y actualización real d'os paquets se prueba per aplicación,
versión y sistema. Las versions minimas de los manifests son declarations
de compatibilidat, no pruebas feitas en todas las versions.
