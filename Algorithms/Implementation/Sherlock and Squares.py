# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:26:14 2017

@author: User
"""

n = int(raw_input())

for s in range(n):
    counter = 0
    a, b = map(int, raw_input().strip().split())
    a, b = pow(a, 0.5), pow(b, 0.5)
    if int(a) == a:
        print int(b)-int(a)+1
    else:
        print int(b)-int(a)