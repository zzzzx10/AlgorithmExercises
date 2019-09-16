# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:54:38 2019

用两个队列实现栈
"""

class Solution:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.q2:
            self.q1.append(self.q2.pop(0))
        self.q1.append(x)

        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.q2:
            self.q1.append(self.q2.pop(0))
        if self.q1:
            while len(self.q1)>1:
                #print("appe",self.q1,self.q2)
                self.q2.append(self.q1.pop(0))
                #print(self.q1,self.q2)
            return self.q1.pop(0)
            
        

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.q2:
            self.q1.append(self.q2.pop(0))
        return self.q1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return (not self.q1) and (not self.q2)


P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop(),P.top(),P.empty())
print(P.pop(),P.top(),P.empty())
#print(P.pop(),P.top(),P.empty())
print(P.pop())