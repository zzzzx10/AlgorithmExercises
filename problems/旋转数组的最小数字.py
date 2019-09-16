# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:48:36 2019

旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        if rotateArray[right] > rotateArray[left]:
            return rotateArray[0]

        while left <= right:
            if right-left == 1:
                return rotateArray[right] 
            mid = (left + right) // 2
            if rotateArray[right] < rotateArray[mid]:
                left = mid
            else:
                right = mid

          
s = Solution()
print(s.minNumberInRotateArray([3,4,5,1,2]))
print(s.minNumberInRotateArray([1,2,3,4,5]))
print(s.minNumberInRotateArray([1,0,1,1,1]))
print(s.minNumberInRotateArray([4,5,6,7,0,1,2]))
