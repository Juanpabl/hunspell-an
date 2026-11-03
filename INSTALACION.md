# Instalación d'o corrector aragonés 1.0.0

Esta carpeta contiene los fuentes d’a candidata. Lo OXT citau contino ye un artefacto local de pruebas, no una descarga publicada en GitHub.

## LibreOffice

1. Ubrir lo chestor d'extensions de LibreOffice.
2. Triar Anyadir y triar `corrector-ortografico-aragones.1.0.0.oxt`.
3. Completar la instalación y reiniciar LibreOffice.
4. Asignar l'idioma aragonés a lo texto y activar la revisión ortografica.

L'identificador permanent d'a extensión ye `org.aragones.hunspell.aal`. Pa actualizar versions futuras d'esta extensión, instalar lo nuevo OXT dende lo mesmo chestor.

Si i hai unatro diccionario aragonés instalau, desactivar-lo u retirar-lo pa privar que toz dos interviengan en a comprebación.

La revisión ortografica puede veyer-se influyida per l'idioma d'o texto y per las parolas anyadidas a lo diccionario personal. Comprebar los dos achustes si los resultaus son inasperaus.

## Hunspell y otras aplicaciones

Lo par `an_ES.dic` y `an_ES.aff` ye codificau en UTF-8; mantener ambos archivos chuntos y con o mismo nombre base. Per eixemplo, dende este directorio puet lanzar-se:

```sh
hunspell -i UTF-8 --no-default-personal -d ./an_ES -l texto.txt
```

Esta candidata s'ha comprebau con Hunspell nativo 1.7.2. La instalación y la segmentación d'esta versión exacta en LibreOffice/Windows, Firefox y atras aplicacions requieren una prueba propia.

Lo texto ye UTF-8 y los identificadors d’afixos son numericos (FLAG num).
OpenOffice requiere que la versión instalada reconoixca aragonés como idioma.
