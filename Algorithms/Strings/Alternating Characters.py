# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:36:10 2017

@author: User
"""

n = int(raw_input())
for i in range(n):
    s = raw_input()
    last = s[0]
    count = 0
    for l in range(1,len(s)):
        if s[l] == last:
            count += 1
        else:
            last = s[l]
    print count