#!/usr/bin/python3

import re

regex = input("Enter a regular expression: ")
file = "code/mbox.txt"

fd = open(file, 'r')

count = 0
for line in fd:
    if re.search(regex, line):
        count += 1

fd.close()

print("%s had %d lines that matched %s" % (file, count, regex))