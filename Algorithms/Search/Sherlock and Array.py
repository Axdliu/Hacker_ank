# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:42:28 2017

@author: User
"""

def test(k, s):
    sum_s = sum(s)
    add = 0
    for i in range(k):
        #print s[i], add
        if (sum_s - 2*add) == s[i]:
            return 'YES'
        else:
            add += s[i]
    return 'NO'

n = int(raw_input())

for i in range(n):
    k = int(raw_input())
    s = map(int, raw_input().strip().split())
    print test(k, s)