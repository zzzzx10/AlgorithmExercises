# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:59:04 2019

二叉树的下一个节点 - 中序遍历
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        nNode = pNode
        if pNode.right:
            nNode = pNode.right
            while nNode.left:
                nNode = nNode.left
            return nNode
        
        while nNode.next:
            if nNode.next.left == nNode:
                return nNode.next
            else:
                nNode = nNode.next
        return None

'''
    1
   / \
  2   3
 / \
4   5

'''
n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n4 = TreeLinkNode(4)
n5 = TreeLinkNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5 
n4.next = n2
n5.next = n2
n2.next = n1
s = Solution()       
print(s.GetNext(n5).val)