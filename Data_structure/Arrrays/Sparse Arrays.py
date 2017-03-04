# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:57:37 2017

@author: User
"""

N = int(raw_input())
strings = []
for i in range(N):
    strings.append(raw_input())
Q = int(raw_input())
for i in range(Q):
    query = raw_input()
    print len([k for k,x in enumerate(strings) if x == query])