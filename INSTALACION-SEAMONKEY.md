# Corrector aragonés 1.1.0 pa SeaMonkey

Paquet: corrector-ortografico-aragones.1.1.0-seamonkey.xpi.

Diccionario clásico con install.rdf (tipo 64), exclusivament pa SeaMonkey.
Conserva l'identificador hunspell-an-seamonkey@juanpabl.github.io y los nombres
dictionaries/an.dic y dictionaries/an.aff. Lo par coincide byte a byte con
an_ES.dic y an_ES.aff. No ye lo paquet WebExtension de Thunderbird.

Lo manifiesto declara SeaMonkey 2.53.x. La integridat d'o paquet y la instalación
real se comprueban per separau; no atribuir a 1.1.0 pruebas de paquets anteriors.

## Instalación y actualización

1. Ubrir lo chestor de complementos y seleccionar Instalar complemento desde archivo.
2. Seleccionar lo XPI y reiniciar SeaMonkey si lo pide.
3. Comprobar que figura la versión 1.1.0 y seleccionar Aragonés pa la revisión.
4. Prebar las parolas d'INSTALACION.md y rechistrar versión, sistema y resultau.
5. Repetir con una instalación anterior de la mesma extensión pa prebar l'actualización.

Las fichas u identificadors diferents d'extensions antigas no s'actualizan
entre sí automaticament.

## Reconstrucción

```sh
python mozilla/build_seamonkey.py . /ruta/ta/paquets
```

Lo constructor leye mozilla/seamonkey/install.rdf. Los paquets definitivos
s'acompanyan de sus propias sumas SHA-256.
