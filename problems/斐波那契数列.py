# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:31:54 2019

斐波那契数列

现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）
f(n) =  0               n = 0
        1               n = 1
        f(n-1)+f(n-2)   n > 1

应用情景：
1.青蛙跳台阶问题，一只青蛙一次可以跳1级台阶，也可以跳2级，
想要跳n级，一共有多少种方法
2. 2x1小矩形覆盖2x8矩形
"""

class Solution:
    def Fibonacci(self, n):
        # write code here
        num = [0,1]
        if n > 1:
            for i in range(2,n+1):
                num.append(num[i-1] + num[i-2])
        return num[n]
        
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        a = 0
        b = 1
        for _ in range(2,N+1):
            a, b = b, a+b
        return b

s = Solution()
print(s.Fibonacci(4))
print(s.fib(10))