#!/usr/bin/python3

import string

file = 'code/mbox.txt'
try:
    fd = open(file)
except:
    print('There is not such a file %s.' % (file))
    exit()

Dict = dict()
for line in fd:
    if not line.startswith("From "): continue
    email = line.split()[1]
    Dict[email] = Dict.get(email, 0) + 1

lst = list()
for key, value in Dict.items():
    lst.append(( value, key ))

lst.sort(reverse=True)
print(lst[0][1] + ' ' + str(lst[0][0]))

fd.close()
