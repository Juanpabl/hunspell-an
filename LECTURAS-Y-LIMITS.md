# Lecturas y limits d'a 0.4.0

La revisión verifica apostrofacions y la autorización morfolochica d'encliticos.
No certifica cada posible contexto sintactico ni revisa exhaustivament lo lexico.
Apertium s'emplega como referencia fixada de metadatos, sin importación masiva.

Una cadena puede tener lectura nominal y verbal; se conserva si tiene una
lectura válida. La segmentación por guión se mantiene por decisión expresa.
Lo motor y la interficie d'una aplicación se prueban per separau.

La cobertura lexica heredada tamién tiene omisions: por exemplo, escritoras no
se reconoixe ni en la base 0.3.0 ni en esta candidata. No se presenta como una
regresión introducida por esta revisión; corresponde revisar la flexión y
cobertura sistematica en la fase d'Apertium. Las pruebas manuals emplegan
formas admitidas per lo diccionario pa no atribuir una falta de cobertura a
una regla d'apostrofación.

Espera tiene una lectura femenina nominal y otra verbal analizable (variante
de aspera). Se conserva l'espera, ya admitida en 0.3.0, como lectura verbal
posible, sin ampliar las combinacions d'atros pronombres ni transmitir l' a
la flexión nominal. La flag p queda restrinchida a ixa forma. La decisión
lexica sobre las variantes exclusivas d'análisis corresponde a la fase 1.
