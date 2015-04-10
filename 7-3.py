#!/usr/bin/python3

file = input("Enter file name: ")
if file == '':
    file = "code/mbox-short.txt"
elif file == 'na na boo boo':
    print(file.upper() + ' - ' + "You have been punk'd!")
    exit()

try:
    fhand = open(file)
except:
    print("File \"%s\" does not exist." % file)
    exit()

count = 0
num = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        start_pos = line.find(':') + 1
        line = line.rstrip()
        spam = line[start_pos:].lstrip()
        try:
            spam = float(spam)
        except:
            continue
        count += 1
        num += spam

spam_avg = str(num / count)
print("Average spam confidence: " + spam_avg)
