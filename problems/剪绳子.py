# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:25:18 2019

给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""

class Solution:
    def cutRope(self, number):
        # write code here
        # 贪婪算法解法，n>=5时，3(n-3)>=2(n-2)
        if number < 2:
            return 0
        ori = [1,2,4]
        if number <= 4:
            return ori[number-2]
        
        leftonly = [0,1,2,3]
        left = number
        multi = 1
        while left >= 4:
            left -= 3
            multi *= 3
        multi = multi*leftonly[left]
        return multi
    
    def cutRope2(self,number):
        #动态规划
        if number < 2:
            return 0
        ori = [1,2]
        if number <= 3:
            return ori[number-2]
        
        dp = [1]*number
        dp[:3] = [0,1,2,3]
        for i in range(3,number+1):
            for j in range(1, i//2 + 1):
                dp[i] = max(dp[i],dp[i-j]*j)
                #print(i,j,dp)
        return dp[number]
        
    
s = Solution()
print(s.cutRope(9))
print(s.cutRope2(9))