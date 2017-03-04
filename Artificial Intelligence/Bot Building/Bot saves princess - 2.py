# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:03:49 2017

@author: User
"""

def nextMove(n,r,c,grid):
    m = (r, c)
    for r1 in xrange(n):
        for c1 in xrange(n):
            if grid[r1][c1] == 'p':
                p = (r1, c1)
    distance = (m[0]-p[0], m[1]-p[1])
    if distance[1] == 0 :
        if distance[0] > 0:
            return 'UP'
        else:
            return 'DOWN'
    elif distance[0] == 0 :
        if distance[1] > 0:
            return 'LEFT'
        else:
            return 'RIGHT'
    else:
        if distance[0] > 0:
            return 'UP'
        else:
            return 'DOWN'
        

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
