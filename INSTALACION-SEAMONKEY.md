# Corrector aragonés 0.4.0 pa SeaMonkey

Paquet: `corrector-ortografico-aragones.0.4.0-seamonkey.xpi`.

Ye un diccionario clásico con `install.rdf` (tipo 64), sin scripts,
exclusivament pa SeaMonkey. Emplega l'identificador propio
`hunspell-an-seamonkey@juanpabl.github.io` y lo código `an` en los
nombres d'o par `dictionaries/an.dic` y `dictionaries/an.aff`.
Lo conteniu lingüistico coincide byte a byte con `an_ES.dic` y `an_ES.aff`.

## Estau y compatibilidat

Preparau pa SeaMonkey **2.53.x**. S'ha verificau la integridat ZIP,
lo XML d'o manifiesto, lo destino SeaMonkey y los fichers d'o diccionario.
**Encara no s'ha prebau la instalación en SeaMonkey.** Lo paquet ye un
candidato pa prebas antes de puyar-lo al catalogo; no contiene firma digital.

## Preba d'instalación

1. Ubrir lo chestor de complementos de SeaMonkey, en Ferramientas.
2. Emplegar Instalar complemento desde archivo y seleccionar lo `.xpi`.
3. Reiniciar SeaMonkey si lo pide y comprobar que figura la versión 0.4.0.
4. En un campo de texto multilínia, activar la revisión ortografica y
   seleccionar Aragonés. Se puede prebar tamién redactando un mensache.
5. Con solo lo diccionario aragonés activau, escribir:

```text
charrábaz chóvens árbols diré puedo saldré me'n
zzzxqvzz
```

Las formas d'a primera línia deberían estar acceptadas y `zzzxqvzz`, marcada.
Pa `metesetz`, comprobar que propone `metésez`. Registrar la versión exacta
de SeaMonkey y las prebas feitas. Si bi ha lo diccionario antiguo instalau,
desactivar-lo pa que no interfiera con lo nuevo. Emplegar un perfil de prebas.

## Publicación

En Thunderbird Add-ons, crear una **nueva ficha** pa este diccionario clásico
y seleccionar solo **SeaMonkey**. Nombre proposau:
**Corrector ortografico aragonés — SeaMonkey**.

Lo catalogo no permite actualizar una ficha WebExtension con un paquet
clásico. Por ixo esta ficha y l'identificador son separaus de Thunderbird.
Los usuarios d'o diccionario antiguo deberán instalar lo nuevo y retirar
u desactivar l'antiguo; no recibirán una actualización automatica entre fichas.

Chestor: https://addons.thunderbird.net/developers/

## Reconstrucción

Dende lo directorio d'a distribución, con Python 3:

```sh
python mozilla/build_seamonkey.py . .
```

Dimpués de reconstruir, recalcular `SHA256SUMS.txt`.

Referencia: https://www.seamonkey-project.org/dev/extensions
