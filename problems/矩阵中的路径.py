# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:00:50 2019

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 
a b c e 
s f c s
a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

class Solution:
    def exist(self, board, word) -> bool:
        width = len(board[0])
        height = len(board)
        
        
        def spread(i,j,w): 
            if not w:
                return True
            #print("spread",i,j,w)
            original, board[i][j] = board[i][j], '-'
            spreaded = False
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                #print("for",x,y)
                if (0<=x<height and 0<=y<width and w[0]==board[x][y] and spread(x, y, w[1:])):
                    spreaded = True
                    break
            board[i][j] = original
            return spreaded

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    print(i,j)
                    if spread(i,j,word[1:]):
                        return True
                    
        return False

s = Solution()

board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']
        ]
print(s.exist(board,"ABCCED"))
print(s.exist(board,"SEE"))
print(s.exist(board,"ABCB"))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
print(s.exist(board,"AAB"))
board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
print(s.exist(board,"ABCEFSADEESE"))