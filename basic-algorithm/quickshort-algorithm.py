import os, sys, math


def quickshort(quickArr):
    if len(quickArr) <= 1:
        return quickArr
    pivot = quickArr[len(quickArr) // 2]
    left = [x for x in quickArr if x < pivot]
    middle = [x for x in quickArr if x == pivot]
    right = [x for x in quickArr if x > pivot]
    return quickshort(left) + middle + quickshort(right)

arrQuick = [3, 6, 8, 10, 1, 2, 1]
print(quickshort(arrQuick))