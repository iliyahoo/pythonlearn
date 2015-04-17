#!/usr/bin/python3

import string

file = 'code/mbox-short.txt'
try:
    fd = open(file)
except:
    print('There is not such a file %s.' % (file))
    exit()

Dict = dict()
for line in fd:
    if not line.startswith('From '): continue
    line = line.split()
    date = line[5]
    hour = date.split(':')[0]
    Dict[hour] = Dict.get(hour, 0) + 1

lst = list()
for key, val in Dict.items():
    lst.append(( key, val ))

lst.sort()
for key, val in lst:
    print(key + ' ' + str(val))

fd.close()
