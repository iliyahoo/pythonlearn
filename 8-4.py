#!/usr/bin/python3

fh = open('code/romeo.txt')
#list = []
#
#for line in fh:
#    line = line.split()
#    for word in line:
#        if word in list: continue
#        else: list.append(word)
#
#list.sort()
#print(list)


lst = list()
for line in fh:
    line = line.split()
    for word in line:
        if word in lst: continue
        else: lst.append(word)
lst.sort()
print(lst)