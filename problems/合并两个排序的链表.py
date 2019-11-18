# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:19:07 2019

@author: Administrator
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        c = ListNode(0)
        comb = c
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                
                c.next = pHead1
                c = c.next
                pHead1 = pHead1.next
            else:
                c.next = pHead2
                c = c.next
                pHead2 = pHead2.next
        if not pHead2:
            c.next = pHead1
        else:
            c.next = pHead2
        return comb.next
     
l = ListNode(0)
l1 = l
l.next =  ListNode(1)
l = l.next
l.next =  ListNode(2)

n = ListNode(1)
n1 = n
n.next =  ListNode(2)
n = n.next
n.next =  ListNode(4)

s = Solution()
print(s.Merge(l1,n1).val)