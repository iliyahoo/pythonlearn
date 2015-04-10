#!/usr/bin/python3

file = input("Enter a file name: ")
if len(file) == 0: file = 'code/mbox.txt'

try:
    fd = open(file)
except:
    print("File %s is not exist." % (file))
    exit()

Dict = dict()
keys_list = []
values_list = []

for line in fd:
    if line.startswith('From '):
        line = line.split()
        mail = line[1]
        Dict[mail] = Dict.get(mail, 0) + 1

# divide the keys from values
for mail in Dict:
    keys_list.append(mail)
    values_list.append(Dict[mail])
index = values_list.index(max(values_list))

print(keys_list[index], values_list[index])
#print(Dict)