#!/usr/bin/python3

import sys

#file = input("Enter file name: ")
file = "code/mbox-short.txt"

try:
    fhand = open(file)
except:
    print("File %s does not exist." % file)
    sys.exit()

for line in fhand:
    line = line.rstrip().upper()
    print(line)
