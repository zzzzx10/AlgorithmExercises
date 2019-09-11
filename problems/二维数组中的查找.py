# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:33:34 2019

二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = len(array[0])-1
        while i <= len(array)-1 and j >= 0 :
                print(i,j,array[i][j])
                if array[i][j] == target:
                    return True
                elif array[i][j] > target:
                    j -= 1
                else:
                    i += 1
        return False

    
    def test(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(self.Find(5,a))
        print(self.Find(11,a))
        a = [[1, 2,8,9], [2,4,9,12], [4,7,10,13],[6,8,11,15]]
        print(self.Find(5,a))
        print(self.Find(11,a))
        

s = Solution()
s.test()