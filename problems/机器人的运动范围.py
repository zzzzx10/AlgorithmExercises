# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:28:40 2019

地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def ok(i,j):
            num = [x for x in str(i)+str(j)]
            num = list(map(int,num))
            return True if sum(num)<=threshold else False

        
        def spread(i,j):
            self.count+=1
            blocks[i][j]=1
            #print(i,j,self.count,blocks)
            for x,y in (((i-1),j),(i,(j-1)),((i+1),j),(i,(j+1))):
                if 0<=x<rows and 0<=y<cols and blocks[x][y]==0 and ok(x,y):
                    spread(x,y)
                    
            
        blocks = [[0]*cols for _ in range(rows)]
        self.count = 0
        if threshold > 0:
            spread(0,0)
        return self.count
        
s = Solution()
print(s.movingCount(2,2,2))