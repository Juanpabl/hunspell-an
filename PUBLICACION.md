# Preparar y publicar 1.1.0

## Antes de publicar

1. Revisar lo patch de preparación contra lo HEAD actual y las notas 1.1.0.
2. Construyir los paquets dende una copia exacta d'os fuentes revisaus:

```sh
python build_release.py . /ruta/ta/paquets-1.1.0
```

3. Prebar instalación nueva y actualización dende 1.0.0 en las aplicacions.
   Rechistrar versiones, sistemas, reconocimiento y segmentación.
4. Pa Firefox, obtener y verificar la copia firmada. Lo constructor local
   produce lo XPI -unsigned; no s'ha de presentar como copia firmada.
5. Recalcular las sumas d'os artefactos definitivos después de cualsequier
   cambio u firma. SHA256SUMS.txt d'a raíz corresponde a los fuentes;
   SHA256SUMS-PAQUETS.txt corresponde a los paquets locales construyidos.

## Publicación

Dimpués d'aprebar las pruebas, fer lo commit de preparación y la etiqueta
v1.1.0 sobre ixe commit. Crear la release en GitHub con
RELEASE-NOTES-1.1.0.md y adjuntar:

- corrector-ortografico-aragones.1.1.0.oxt
- corrector-ortografico-aragones.1.1.0-firefox.xpi (firmau)
- corrector-ortografico-aragones.1.1.0-thunderbird.xpi
- corrector-ortografico-aragones.1.1.0-seamonkey.xpi
- hunspell-an-1.1.0.tar.gz
- sumas SHA-256 d'os artefactos definitivos

Los nombres locales con -unsigned se conservan mientras no se sustituyan
por las copias definitivas. No renombrar lo XPI de Firefox como firmau sin
comprobar la copia recibida.

Actualizar per separau los catalogos de LibreOffice, Firefox, Thunderbird y
SeaMonkey. La publicación de GitHub no actualiza ixos catalogos ni las copias
incluyidas en distribucions Linux u LibreOffice.

No reconstruyir ni sustituir los artefactos históricos de 1.0.0.
