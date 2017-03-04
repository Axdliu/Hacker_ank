# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:37:20 2017

@author: User
"""


import string

n = int(raw_input())

lists = string.lowercase
code = {}
for x in range(26):
    code[lists[x]] = x

for i in range(n):
    s = raw_input().strip()
    s_len = len(s)
    mid = s_len//2
    counter = 0
    if mid*2 != s_len:
        for n in range(0, mid):
            #print s[mid+n+1], s[mid-n-1]
            counter += abs(code[s[mid+n+1]]-code[s[mid-n-1]])
    else:    
        for n in range(0, mid):
            #print s[mid+n], s[mid-n-1]
            counter += abs(code[s[mid+n]]-code[s[mid-n-1]])
    print counter  