#!/usr/bin/python3.8

import sys

f = open(str(sys.argv[1]), "r")
text = f.read()
print (text)
f.close()
