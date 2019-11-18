# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:32:06 2019

@author: Administrator
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isReverse(n1,n2):
            if (not n1) and (not n2):
                print("None")
                return True
            if (not n1) or (not n2):
                print("nor")
                return False
            print(n1.val,n2.val)
            if n1.val != n2.val:
                print("!=")
                return False
            flag = True
            #if n1.left and n2.right:
            flag = flag and isReverse(n1.left,n2.right)
            #if n1.right and n2.left:
            flag = flag and isReverse(n1.right,n2.left)
            return flag
        
        if root.left and root.right:
            return isReverse(root.left,root.right)
        elif root.left or root.right:
            return False
        else:
            return True
        
'''
    1
   / \
  2   3
 / \
4   5

'''
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
#n2.left = TreeNode(4)
n2.right = TreeNode(3)
#n3.left = TreeNode(3)
n3.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(n1))   