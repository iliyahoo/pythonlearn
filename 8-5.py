#!/usr/bin/python3

file = input("Enter a file name: ")
if len(file) == 0 : file = 'code/mbox-short.txt'

try:
    fh = open(file)
except:
    print("No such file or directory: %s" % (file))
    exit()

count = 0

for line in fh:
    if len(line) == 0 or not line.startswith('From '): continue
    words = line.split()
    print(words[1])
    count +=1

print("There were %d lines in the file with From as the first word" % (count))