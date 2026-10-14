# Instalación en Linux / Hunspell

## Paquet d'a distribución

En Debian y Ubuntu, lo motor y lo diccionario aragonés pueden instalar-se con:

```sh
sudo apt install hunspell hunspell-an
hunspell -D
```

La versión de `hunspell-an` disponible depende d'a distribución y puede
contener un diccionario anterior a la versión 0.3.0. La numeración d'o
paquet puede corresponder a la colección de LibreOffice, no a la versión
d'o diccionario aragonés. Pa emplegar expresament esta entrega, sigue
la instalación manual.

## Descargar la versión 0.3.0

Cal tener lo executable `hunspell`, `curl` y `tar`. En Debian/Ubuntu:

```sh
sudo apt install hunspell curl tar
```

Dende una carpeta de descargas u de treballo:

```sh
curl -fLO https://github.com/Juanpabl/hunspell-an/releases/download/v0.3.0/hunspell-an-0.3.0.tar.gz
tar -xzf hunspell-an-0.3.0.tar.gz
```

Lo paquet crea `hunspell-an-0.3.0/`, con los dos fichers d'o diccionario,
lo README, estas instrucciones, licencia y textos completos d'as licencias.

Pa verificar lo conteniu extraito:

```sh
(cd hunspell-an-0.3.0 && sha256sum -c SHA256SUMS.txt)
```

Las sumas detectan alteracions d'os fichers; no son una firma digital.
Lo `SHA256SUMS.txt` d'a Release permite verificar tamién lo archivo `.tar.gz`.

## Instalación pa lo tuyo usuario

Dende la carpeta donde has extraito lo paquet:

```sh
mkdir -p "$HOME/.local/share/hunspell"
cp hunspell-an-0.3.0/an_ES.aff hunspell-an-0.3.0/an_ES.dic "$HOME/.local/share/hunspell/"
```

Esta copia instala u reemplaza lo par d'esta ruta de usuario. Lo paquete
de sistema, si en tiens uno, sigue estando en la suya ruta.

Pa prebar esta copia, sin interferencia d'o diccionario personal:

```sh
printf '%s\n' charrábaz chóvens árbols diré puedo saldré zzzxqvzz |
  hunspell -i UTF-8 --no-default-personal -d "$HOME/.local/share/hunspell/an_ES" -l
```

Lo resultau asperau ye solo `zzzxqvzz`.

Pa revisar un fichero UTF-8, executa esta orden dende la carpeta d'o texto:

```sh
hunspell -i UTF-8 --no-default-personal -d "$HOME/.local/share/hunspell/an_ES" -l texto.txt
```

Pa obtener sucherencias, usa `-a`:

```sh
hunspell -i UTF-8 --no-default-personal -d "$HOME/.local/share/hunspell/an_ES" -a < texto.txt
```

La ruta explicita de `-d` ye lo metodo más fiable pa seleccionar esta copia.
Si quiers incorporar esta carpeta a la busca de Hunspell en la terminal actual:

```sh
export DICPATH="$HOME/.local/share/hunspell${DICPATH:+:$DICPATH}"
hunspell -D
```

No totas las aplicaciones consultan esta variable u esta carpeta. Firefox,
Thunderbird y LibreOffice tienen tamién los paquets propios d'o proyecto.

## Pa mantenedors de distribucions

- Proyecto orichinal: https://github.com/Juanpabl/hunspell-an
- Entrega fixa: https://github.com/Juanpabl/hunspell-an/releases/tag/v0.3.0
- Fichers UTF-8: `an_ES.aff` y `an_ES.dic`.
- Licencia alternativa: `MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later`.
- Contacto: `an.spellchecker@gmail.com`.

Los fichers d'o diccionario no requieren compilación pa Hunspell.
Conservar los creditos y las licencias en lo paquet distribuiu.
