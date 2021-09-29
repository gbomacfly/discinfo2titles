#!/usr/bin/env python3
"""
File: discinfo2titles.py
Created Date: 29.09.2021 23:23:31
Author: Sascha Buerk
Email: macfly@german-bash.org
Last Modified: 29.09.2021 23:52:33
"""

__author__ = "Sascha Buerk"
__email__ = "macfly@german-bash.org"
__version__ = 1.0

import configparser

input = "disc.info.ini"
output= "titles.txt"

config = configparser.ConfigParser()

open(output, 'w').close() # Leere Datei erstellen oder Inhalt löschen

f = open(output, "a") # Datei zum anfügen (append) öffnen

config.read(input)

for x in config.sections():
	f.write(x + " = " + config[x]['Original Title'] + "\n")
	print(x + " = " + config[x]['Original Title'])

f.close()

print("All done, output written to {output}".format(output=output))