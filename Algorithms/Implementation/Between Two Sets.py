# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:18:29 2017

@author: User
"""

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

result = 0
for i in range(max(a), min(b)+1):
    counter = 0
    for k in a:
        if i%k == 0:
            counter += 1
    for k in b:
        if k%i == 0:
            counter += 1
    if counter == len(a)+len(b):
        result += 1

print result