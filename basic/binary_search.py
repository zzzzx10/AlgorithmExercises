# -*- coding: utf-8 -*-
"""
二分查找
给出有序元素列表list和查找的item
返回item在list中的位置list[mid]=item
没有则返回None
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2   # // 取整数商
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:  #猜测过大，将high减小到 mid-1
            high = mid - 1
        else:
            low = mid + 1   #猜测过小，将low增加到 mid+1

    # 循环完毕没有返回
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None
