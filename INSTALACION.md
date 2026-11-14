# Instalación d'o corrector aragonés 1.0.0

Esta carpeta contiene los fuentes d’a candidata. Lo OXT citau contino ye un artefacto local de pruebas, no una descarga publicada en GitHub.

## LibreOffice

### LibreOffice 26.8.3 u posterior

Dende LibreOffice **26.8.3**, lo corrector aragonés incluyiu ye la
versión **1.0.0**, adaptada a la ortografía de l’Academia Aragonesa de
la Lengua (AAL).

Si lo diccionario ye instalau, asigna **Aragonés** como luenga d’o texto
y activa la revisión ortografica. En Linux, la disponibilidat
d’o diccionario puede depender d’os paquets instalaus d’a distribución.

### Versions anteriors u instalacions sin lo diccionario

1. Baixa lo `.oxt` 1.0.0 dende lo
   [catálogo oficial d’extensions de LibreOffice](https://extensions.libreoffice.org/en/extensions/show/corrector-ortografico-aragones)
   u dende la [release v1.0.0 en GitHub](https://github.com/Juanpabl/hunspell-an/releases/tag/v1.0.0).
2. Ubre lo chestor d’extensions de LibreOffice, tría **Anyadir** y
   selecciona lo fichero `.oxt`.
3. Reinicia LibreOffice, asigna **Aragonés** como luenga d’o texto y
   activa la revisión ortografica.

Si ya tiens instalau unatro corrector aragonés como extensión, desactiva-lo pa privar interferencias.

## Hunspell y otras aplicaciones

Lo par `an_ES.dic` y `an_ES.aff` ye codificau en UTF-8; mantener ambos archivos chuntos y con o mismo nombre base. Per eixemplo, dende este directorio puet lanzar-se:

```sh
hunspell -i UTF-8 --no-default-personal -d ./an_ES -l texto.txt
```

Esta candidata s'ha comprebau con Hunspell nativo 1.7.2. La instalación y la segmentación d'esta versión exacta en LibreOffice/Windows, Firefox y atras aplicacions requieren una prueba propia.

Lo texto ye UTF-8 y los identificadors d’afixos son numericos (FLAG num).
OpenOffice requiere que la versión instalada reconoixca aragonés como idioma.
