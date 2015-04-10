#!/usr/bin/python3

list = []

while True:
    num = input("Enter a number: ")

    if num.lower() == "done" and len(list) == 0:
        print("There is not any number yet.")
        exit()
    elif num.lower() == "done" and len(list) != 0:
        print("Maximum: " + str(max(list)))
        print("Minimum: " + str(min(list)))
        exit()
    else:
        try: num = float(num)
        except: continue

## first variant
#    list.append(num)

# second variant
    if len(list) == 0: list = [num, num]
    elif list[1] < num: list[1] = num
    elif list[0] > num: list[0] = num
