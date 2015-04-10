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
    line = line.translate(None, string.punctuation)
    line = line.lower()
    line = line.split()
    for word in line:
        Dict[word] = Dict.get(word, 0) + 1

lst = list()
for key, val in Dict.items():
    lst.append(( val, key ))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print('%s: %s' % (key, val))

fd.close()
