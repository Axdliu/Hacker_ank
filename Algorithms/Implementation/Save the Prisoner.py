# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:23:22 2017

@author: User
"""

r = int(raw_input())
for i in range(r):
    n, sweet, start = map(int, raw_input().strip().split())
    S = (sweet+start-1)%n
    if S == 0:
        print n
    else:
        print S