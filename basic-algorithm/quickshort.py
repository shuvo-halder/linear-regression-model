import math, os

def quick_short(arrayShort):
    if len(arrayShort) <= 1:
        return arrayShort
    
    pivot = arrayShort[len(arrayShort) // 2]
    
    left = [x for x in arrayShort if x < pivot]
    middle = [x for x in arrayShort if x == pivot]
    right = [x for x in arrayShort if x > pivot]

    return quick_short(left) + middle + quick_short(right)


# give input and check it work or not

arry = [3, 4, 9, 6, 10, 54, 11, 1, 5, 2, 7]
shorted_array = quick_short(arry)
print(shorted_array)
