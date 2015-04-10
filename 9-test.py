#!/usr/bin/python3

import string
import operator

file = 'code/romeo-full.txt'
Dict = dict()

try:
    fd = open(file)
except:
    print("There is not such a file: %s" % (file))
    exit()

for line in fd:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    for word in line.split():
        Dict[word] = Dict.get(word, 0) + 1
#        if not word.isalpha(): continue

## sort dict by keys
#lst = Dict.keys()
#lst.sort()
#for i in lst:
#    print(i + ': ' + str(Dict[i]))

# sort dict by values using tuples
sorted_Dict = sorted(Dict.items(), key=operator.itemgetter(1))
for i in sorted_Dict:
    print(i[0] + ': ' + str(i[1]))


fd.close()
