# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:03:01 2017

@author: User
"""

#!/bin/python
def displayPathtoPrincess(n,grid):
#print all the moves here
    m = None
    p = None
    for r in xrange(n):
        for c in xrange(n):
            if grid[r][c] == 'm':
                m = (r, c)
            elif grid[r][c] == 'p':
                p = (r, c)
    distance = (int(m[0])-int(p[0]), int(m[1])-int(p[1]))
    if distance[0]>0 :
        for s in range(abs(distance[0])):
            print 'UP'
    else:
        for s in range(abs(distance[0])):
            print 'DOWN'
    if distance[1]>0 :
        for s in range(abs(distance[1])):
            print 'LEFT'
    else:
        for s in range(abs(distance[1])):
            print 'RIGHT'

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())
    
displayPathtoPrincess(m,grid)