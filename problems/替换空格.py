# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:08:56 2019

请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。

本题的主要考察点实际上是，在合并字符串/数组时，
如果从前往后复制每个数，可能需要重复移动某些数字
此时，考虑从后往前复制，这样就可以减少移动次数，提高效率
"""

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = ['%20' if x==' ' else x for x in s]
        s = ''.join(s)
        
        # s = s.replace(' ', '%20')
        # s = "%20".join(list(s.split(" ")))
        return s
        
    def test(self):
        a = "We Are Happy"
        print(self.replaceSpace(a))
        

s = Solution()
s.test()