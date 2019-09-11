# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:46:55 2019

找出数组中重复的数字

1.在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3},那么对应的输出是重复的数字2或者3。

2. 不修改数组找出重复数字
长度n+1的数组里，所有数字都在1~n的范围内。找出任一重复的数字
如果输入长度为8的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        
        for i in range(len(numbers)):
        #for i, num in enumerate(nums): 这样分开写也不会有下标更新问题了
            
            # 这两行其实没必要写啊
            if numbers[i] == i:
                continue
            
            while (numbers[i] != i):
                #print(numbers,i)
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[i]
                    return True,duplication[0]
                temp = numbers[i]
                numbers[i] = numbers[numbers[i]] 
                numbers[temp] = temp
                #print(numbers)
        return False
    
    def getDuplicate(self,numbers):
        #不修改数组找出重复数字,该方法不是100%有效
        def countRange(start,mid):
            count = 0
            for n in numbers:
                if n>=start and n<=mid:
                    count +=1
            return count
        
        start = 1 #范围从1开始
        end = len(numbers)-1  #最大值是len-1
        while(start < end):
            mid = (start + end) // 2
            count = countRange(start,mid)
            if start == mid:
                if count > 1:
                    return start
                else:
                    return -1;
            if count > (mid-start+1) :
                end = mid
            else:
                start = mid + 1
        return -1       
            
        
    def test(self):
        a = [1]
        print(self.duplicate([2,3,1,0,2,5,3],a))
        print(self.duplicate([1,2,3,4,5,0,6,7],a))
        print(self.getDuplicate([2,3,5,4,3,2,6,7]))
        print(self.getDuplicate([1,2,3,4,5,6,2]))
       
                
s = Solution()
s.test()
