#!/usr/bin/python3

def chop(list):

# wrong method
# creates the new list
    print(id(list))
    list = list[1:-1]
    print(id(list))

## second method
#    list.pop(0)
#    list.pop(-1)

## third method
#    del list[0]
#    del list[-1]

    return None

def middle(list):
    return(list[1:-1])

p = chop([1,2,3,4,5])
t = middle([1,2,3,4,5])
print(p, t)
