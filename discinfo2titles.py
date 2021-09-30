#!/usr/bin/env python3
"""
File: discinfo2titles.py
Created Date: 29.09.2021 23:23:31
Author: Sascha Buerk
Email: macfly@german-bash.org
License: GPL-3.0-only
Last Modified: 30.09.2021 04:53:10
"""

__author__ = "Sascha Buerk"
__email__ = "macfly@german-bash.org"
__license__ = "GPLv3"
__version__ = 1.0

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
parser.add_argument('-v', '--verbose', action='store_true', help='More Output')
parser.add_argument('-d', '--delete', action='store_true',
                    help='delete disc.info after converting')
args = parser.parse_args()

inputpath = args.file
tmppath = "/tmp/" + inputfile
input = tmppath

try:
    copyfile(inputpath, input)  # copy input to tmp

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

    print("All done, output written to {output}".format(output=output))
    exit(0)

# error handling
except FileNotFoundError:
    print("{input} not found.".format(input=inputfile))
    exit(1)
except PermissionError:
    print("{output} not writeable.".format(output=output))
    exit(2)
