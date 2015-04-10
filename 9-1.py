#!/usr/bin/python3

file = 'code/words.txt'
Dict = dict()

try:
    fd = open(file)
except:
    print("There is not such a file.")
    exit()

for line in fd:
    line = line.split()
    for word in line:
        Dict[word] = ""

#vals = Dict.values()
#print("" in vals)
print(Dict)

fd.close()
