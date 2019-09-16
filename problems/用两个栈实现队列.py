# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:04:04 2019

用两个栈来实现一个队列，完成队列的Push和Pop操作。
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.stack1) and (not self.stack2)

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop(),P.empty())
print(P.pop(),P.empty())
print(P.pop(),P.empty())
print(P.pop())