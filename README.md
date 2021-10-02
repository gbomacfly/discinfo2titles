# Discinfo2Titles

[![Generic badge](https://img.shields.io/github/repo-size/gbomacfly/discinfo2titles?style=plastic)](https://shields.io/)
[![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg?style=plastic)](https://github.com/gbomacfly/discinfo2titles/releases/)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/gbomacfly/discinfo2titles)
[![licensebuttons by-sa](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0)


This script is used for converting a `disc.info` generated from `Wii Backup Manager` into a `titles.txt`, which can be read by `Configurable USB Loader`.
  
## Usage

```text
usage: discinfo2titles.py [-h] [-V] [-v] [-d] [file]

Converts a disc.info to titles.txt

positional arguments:
  file           the full path to disc.info (default: disc.info)

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit
  -v, --verbose  more output
  -d, --delete   delete disc.info after converting
  ```

## Example

`discinfo2titles.py -v examples/disc.info`

## License

```text
discinfo2titles © 2021 by Sascha Bürk is licensed under CC BY-SA 4.0

This work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/ or
send a letter to Creative Commons, PO Box 1866,
Mountain View, CA 94042, USA.
```
