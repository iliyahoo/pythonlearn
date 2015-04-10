#!/usr/bin/python3

fh = open('code/mbox-short.txt')
count = 0


for line in fh:

# work with strings
    if len(line) == 0 or not line.startswith('From '): continue
    print(line.rstrip('\n'))

## work with lists
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    print(words)

    count +=1

print('\n' + str(count))