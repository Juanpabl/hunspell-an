# Firefox y Thunderbird — 1.1.0

Emplegar lo paquet especifico de cada aplicación:

- corrector-ortografico-aragones.1.1.0-firefox.xpi: copia firmada pa distribución.
- corrector-ortografico-aragones.1.1.0-thunderbird.xpi: paquet de Thunderbird.

Lo constructor produce XPI con sufixo -unsigned. No s'han de confundir con
lo fichero firmau y definitivu de Firefox. Los paquets contienen lo mesmo
par DIC/AFF que los fuentes; las firmas pueden añadir metadatos al ZIP.


Reconstrucción, dende la raíz d'os fuentes:

```sh
python mozilla/build_mozilla.py . /ruta/ta/paquets
```

Lo script leye los manifests revisaus de mozilla/firefox y mozilla/thunderbird.
