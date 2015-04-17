#!/usr/bin/python3

import string

file = 'code/romeo-full.txt'
try:
    fd = open(file)
except:
    print('There is not such a file %s.' % (file))
    exit()

Dict = dict()
for line in fd:
    line = line.lower()
    for letter in line:
        if not letter.isalpha() : continue
        Dict[letter] = Dict.get(letter, 0) + 1

lst = list()
for key, val in Dict.items():
    lst.append(( val, key ))

lst.sort(reverse=True)

for val, key in lst:
    print('%s: %s' % (key, val))

fd.close()
