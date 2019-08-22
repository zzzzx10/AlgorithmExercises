# -*- coding: utf-8 -*-
"""
快速排序法是平均排序速度最快的排序方法。
定位一个基准值（默认最左），
将数组分成两个子数组：小于基准值的元素和大于基准值的元素
再递归地对这两个子数组进行快速排序。
"""

def quicksort(array):
    if len(array) < 2:
        # 基线条件base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # 递归条件recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))

