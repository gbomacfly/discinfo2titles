# Discinfo2Titles

![GitHub](https://img.shields.io/github/license/gbomacfly/discinfo2titles)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%3F/Yes%21/blue?icon=github)](https://github.com/gbomacfly/discinfo2titles)
![GitHub repo size](https://img.shields.io/github/repo-size/gbomacfly/discinfo2titles)
![GitHub all releases](https://img.shields.io/github/downloads/gbomacfly/discinfo2titles/total)
[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in%20-VSCode-blue)](https://open.vscode.dev/gbomacfly/discinfo2titles)

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
