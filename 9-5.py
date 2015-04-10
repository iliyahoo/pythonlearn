#!/usr/bin/python3

file = input("Enter a file name: ")
if len(file) == 0: file = 'code/mbox-short.txt'

try:
    fd = open(file)
except:
    print("File %s is not exist." % (file))
    exit()

Dict = dict()

for line in fd:
    if line.startswith('From '):
        mail = line.split()[1]
        domain = mail.split('@')[1]
        Dict[domain] = Dict.get(domain, 0) + 1

print(Dict)