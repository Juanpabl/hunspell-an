# Instalación d'o corrector aragonés 1.1.0

Los fuentes son en lo repositorio; los instaladors se distribuyen en
[GitHub Releases](https://github.com/Juanpabl/hunspell-an/releases) y en los
catalogos de cada aplicación. Comprobar que lo paquet corresponde a 1.1.0.

## LibreOffice

1. Baixa corrector-ortografico-aragones.1.1.0.oxt dende GitHub Releases u lo
   [catalogo d'extensions](https://extensions.libreoffice.org/en/extensions/show/corrector-ortografico-aragones).
2. En lo chestor d'extensions, tría Anyadir y selecciona lo OXT.
3. Si ya i hai una versión anterior d'esta extensión, confirma l'actualización.
4. Reinicia LibreOffice si lo pide; asigna aragonés como luenga d'o texto
   y activa la revisión ortografica.
5. Compreba que lo chestor amuestra la versión 1.1.0.

Lo diccionario incluyiu con LibreOffice u con la distribución Linux puede
estar anterior. Publicar lo OXT no actualiza automaticament ixas copias.
Si tiens instalau unatro corrector aragonés diferent, desactiva-lo pa evitar
interferencias. Se conserva l'identificador de la extensión d'as versions
anteriors pa permitir l'actualización d'o mesmo complement.

## Hunspell

Mantener an_ES.dic y an_ES.aff chuntos, en UTF-8 y con lo mesmo nombre base:

```sh
hunspell -i UTF-8 --no-default-personal -d ./an_ES -l texto.txt
```

Se veiga INSTALACION-LINUX.md pa la instalación local. Se conserva FLAG num.

## Firefox, Thunderbird y SeaMonkey

Se veiga INSTALACION-MOZILLA.md y INSTALACION-SEAMONKEY.md.
Los tres paquets XPI no son intercambiables.

## Preba d'instalación y actualización

Prebar tanto una instalación nueva como una actualización dende 1.0.0.
Comprobar la versión visible y, con sólo lo corrector aragonés activau:

```text
charrábaz chóvens árbols marguin márguins examen exámens
estremoleixer humedir tintineyo replecar xucar
zzzxqvzz
```

Las dos primeras linias han d'estar acceptadas y zzzxqvzz, marcada.
Comprobar tamién l'aragonés y l’aragonés, y que l'ixeta no s'accepte como
apostrofación d'o diccionario. Si l'aplicación separa las parolas, anotar-lo:
una diferencia de segmentación no ye automaticament un error d'Hunspell.

La batería nativa ye documentada en tests/VERIFICACION.json. Las pruebas
manuals de la versión exacta de LibreOffice, Firefox u atras aplicacions
se rechistran per separau, con versión, sistema y resultau.
OpenOffice requiere que la versión instalada reconoixca aragonés como idioma.
