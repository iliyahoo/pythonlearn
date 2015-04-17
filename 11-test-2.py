#!/usr/bin/python3

import re

file = 'code/mbox-short.txt'
fd = open(file, 'r')

for line in fd:
    line = line.rstrip()
    hour = re.findall('^Details: http[s]?://\S+.\S+/\S+rev=([0-9]{1,})$', line)
    if len(hour) == 0: continue

    print(hour)

fd.close()
