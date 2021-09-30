# Discinfo2Titles

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

Copyright (C) 2021 Sascha Buerk
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
