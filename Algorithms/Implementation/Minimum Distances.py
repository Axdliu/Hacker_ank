# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:31:13 2017

@author: User
"""

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

book = {}
result = []
for i in range(n):
    if A[i] in book.keys():
        result.append(abs(i-book[A[i]]))
        book[A[i]] = i
    else:
        book[A[i]] = i
if len(result) == 0:
    print -1
else:
    print min(result)