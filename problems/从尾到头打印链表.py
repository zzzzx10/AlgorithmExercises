# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:25:55 2019

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

思路：后进先出，用栈来实现这种顺序；用递归，输出后面的节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []  
        while(listNode is not None):
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]        
    

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(singleNode))    