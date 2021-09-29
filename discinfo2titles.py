#!/usr/bin/env python3
"""
File: discinfo2titles.py
Created Date: 29.09.2021 23:23:31
Author: Sascha Buerk
Email: macfly@german-bash.org
Last Modified: 30.09.2021 01:07:46
"""

__author__ = "Sascha Buerk"
__email__ = "macfly@german-bash.org"
__version__ = 1.0

import configparser
import argparse
import os


### Arguments
parser = argparse.ArgumentParser(description='Converts a disc.info to titles.txt')
parser.add_argument('-V', '--version', action='version', version='%(prog)s {v}'.format(v=__version__))
parser.add_argument('-v', '--verbose', action='store_true', help='More Output')
parser.add_argument('-p', '--preserve', action='store_false', help='Don\'t delete disc.info')
args = parser.parse_args()

try:
	### Variables
	input = "disc.info"
	output= "titles.txt"

	### Prepare disc.info
	a_file = open(input, "r")
	lines = a_file.readlines()
	a_file.close()

	if (lines[0] == "\ufeffWBM disc info\n"):
		del lines[:2] # Delete the first two lines

		new_file = open(input, "w+") # Write back to outputfile
		for line in lines:
			new_file.write(line)
		new_file.close()

	open(output, 'w').close() # clear current or make new output file
	f = open(output, "a") # Open output for append

	config = configparser.ConfigParser()
	config.read(input)

	for key in config.sections():
		f.write(key + " = " + config[key]['Original Title'] + "\n")
		if args.verbose: (print(key + " = " + config[key]['Original Title']))
	f.close()

	if args.preserve: os.remove(input)

	print("All done, output written to {output}".format(output=output))
	exit(0)

except FileNotFoundError:
	print("{input} not found.".format(input=input))
	exit(1)
except PermissionError:
	print("{output} not writeable.".format(output=output))
	exit(2)