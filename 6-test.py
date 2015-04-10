#!/usr/bin/python3
# count most repeateble character in the string like count method

s = None
if s is None: print('None')
quit()

str1 = "this is string example....wow!!!"
startpos = str1.rfind('.')
endpos = str1.find("!", startpos)
print(str1[startpos + 1 : endpos])

string = "Hello, world! WWWLLLlWWWW ll"
dict = {}

for letter in string:
    if isinstance(letter, str): letter = letter.lower()
    if dict.get(letter) is None:
        dict[letter] = 1
        maximal = letter
    else:
        dict[letter] += 1
        if dict[maximal] < dict[letter]:
            maximal = letter

print(dict)
print(maximal, dict[maximal])

print(string.count('L'))