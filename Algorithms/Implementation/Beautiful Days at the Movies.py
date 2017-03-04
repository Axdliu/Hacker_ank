# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:22:56 2017

@author: User
"""

start, end, k = map(int, raw_input().strip().split(' '))
counter = 0
for i in range(start, end+1):
    x = abs(i - int(str(i)[::-1]))
    if x % k == 0:
        counter += 1
print counter