# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:04:42 2017

@author: User
"""

def next_move(posr, posc, board):
    n = len(board[0])
    dirt = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'd':
                dirt.append([abs(posr-i)+abs(posc-j),i,j])
    u_d = ('UP', 'DOWN')
    l_r = ('LEFT', 'RIGHT')

    dirt = sorted(dirt, key = lambda x:x[0])
    target = dirt.pop(0)
    while target[0] != 0:
        distance = [posr - target[1], posc - target[2]]
        for r in range(abs(distance[0])):
            target[0] -= 1
            if distance[0]>0:
                print u_d[0]
                return
            else:
                print u_d[1]
                return
        for c in range(abs(distance[1])):
            target[0] -= 1
            if distance[1]>0:
                print l_r[0]
                return
            else:
                print l_r[1]
                return

    print 'CLEAN'
    return

            
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)