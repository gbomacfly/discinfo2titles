#!/usr/bin/env python3
"""
File: discinfo2titles.py
Created Date: 29.09.2021 23:23:31
Author: Sascha Buerk
Email: macfly@german-bash.org
License: CC-BY-SA-4.0
Last Modified: 03.10.2021 00:39:09

Copyright (C) 2021 Sascha Buerk
This work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/ or
send a letter to Creative Commons, PO Box 1866,
Mountain View, CA 94042, USA.
"""

__author__ = "Sascha Buerk"
__email__ = "macfly@german-bash.org"
__license__ = "CC-BY-SA-4.0"
__version__ = 1.2

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
                    version='%(prog)s {v}'.format(v=__version__))
parser.add_argument('-v', '--verbose', action='store_true', help='more output')
parser.add_argument('-a', '--append', action='store_false', default=True,
                    help='append titles.txt instead of overwriting it')
parser.add_argument('-d', '--delete', action='store_true',
                    help='delete disc.info after converting')
args = parser.parse_args()

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
        print("All done, output written to {output}".format(output=output))
    exit(0)

# error handling
except FileNotFoundError:
    print("{input} not found.".format(input=inputfile))
    exit(1)
except PermissionError:
    print("{output} not writeable.".format(output=output))
    exit(2)
