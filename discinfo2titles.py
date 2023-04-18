#!/usr/bin/env python3
"""
Filename: discinfo2titles.py
Created Date: 20.03.2023 10:43:53
Author: Sascha Buerk
Email: macfly@german-bash.org
License: GPL-3.0-or-later
Last Modified: 18.04.2023 02:17:29

Copyright (C) 2023 Sascha Bürk <macfly@german-bash.org>
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will beuseful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.
"""
__author__ = "Sascha Buerk"
__email__ = "macfly@german-bash.org"
__license__ = "GPL-3.0-or-later"
__version__ = 1.3

import configparser
import argparse
import os
from shutil import copyfile

# Variables
inputfile = "disc.info"
output = "titles.txt"

# Arguments
parser = argparse.ArgumentParser(
    description='Converts a disc.info to titles.txt')
parser.add_argument('file', metavar='file', nargs='?',
                    default=inputfile, help='the full path to disc.info (default: %(default)s)')
parser.add_argument('-V', '--version', action='version',
                    version='%(prog)s {}'.format(__version__))
parser.add_argument('-v', '--verbose', action='store_true', help='more output')
parser.add_argument('-a', '--append', action='store_false', default=True,
                    help='append titles.txt instead of overwriting it')
parser.add_argument('-d', '--delete', action='store_true',
                    help='delete disc.info after converting')
args = parser.parse_args([])

tmppath = "/tmp/" + inputfile
input = tmppath

try:
    copyfile(args.file, input)  # copy input to tmp

    # Prepare disc.info
    a_file = open(input, "r")
    lines = a_file.readlines()
    a_file.close()

    if (lines[0] == "\ufeffWBM disc info\n"):
        del lines[:2]  # delete the first two lines

        new_file = open(input, "w+")  # write back to outputfile
        for line in lines:
            new_file.write(line)
        new_file.close()

    if args.append:
        open(output, 'w').close()  # clear current or make new output file
    f = open(output, "a")  # open output for append

    # read disc.info
    config = configparser.ConfigParser()
    config.read(input)

    for key in config.sections():
        f.write(key + " = " + config[key]['Original Title'] + "\n")
        if args.verbose:
            print(key + " = " + config[key]['Original Title'])
    f.close()

    if args.delete:
        os.remove(args.file)

    if args.verbose:
        print("All done, output written to {}".format(output))
    exit(0)

# error handling
except FileNotFoundError:
    print("{} not found.".format(inputfile))
    exit(1)
except PermissionError:
    print("{} not writeable.".format(output))
    exit(2)
