# -*- coding: utf-8 -*-
"""
选择排序
找到当前数组最小值的位置，添加到新数组中
当前代码使用list的pop方法，还可以将当前最小值位置的值，改为超大的数
arr = [5, 3, 6, 2, 10]
a = arr.pop(3)
-> a = 2, arr = [5, 3, 6, 10]
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]      
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) # pop: remove and return item at index _
    return newArr


def selectionSort2(arr):
    INT_MAX = 40
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr[smallest])
        arr[smallest] = INT_MAX
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort2([5, 3, 6, 2, 10]))
