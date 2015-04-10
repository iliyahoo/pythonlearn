#!/usr/bin/python3

import re

file = input("Enter a file name: ")
if len(file) == 0: file = "code/mbox.txt"

regex = '^New Revision: ([0-9]{5})$'

try:
    fd = open(file, 'r')
except:
    print('File does not exist.')
    exit()

lCount = list()
for line in fd:
    result = re.findall(regex, line)
    if len(result) == 0: continue
    lCount += result

fd.close()

for i in range(len(lCount)):
    lCount[i] = int(lCount[i])

average = sum(lCount) / len(lCount)
print(average)
