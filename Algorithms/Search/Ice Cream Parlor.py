# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:40:46 2017

@author: User
"""

n = int(raw_input())

def finder(m, t, f):    
    for h in range(t-1):
        for j in range(h+1, t):
            if f[h]+f[j]== m:
                return str(h+1)+' '+str(j+1) 

for i in range(n):
    m = int(raw_input())
    t = int(raw_input())
    f = map(int, raw_input().strip().split())
    print finder(m, t, f)
    