#!/usr/bin/python3

import re

file = 'code/mbox-short.txt'
fd = open(file, 'r')

dHours = dict()
for line in fd:
    line = line.rstrip()
#    if line.find('From ') != -1:
    hour = re.findall('^From .* (\d{2}):.*', line)
    if len(hour) == 0: continue
    dHours[hour[0]] = dHours.get(hour[0], 0) + 1

lHours = list()
for k, v in dHours.items():
    lHours.append(( str(k), str(v) ))
lHours.sort(reverse=False)

print(dHours)
print(lHours)

for t in lHours:
    print(' '.join(t))

fd.close()
