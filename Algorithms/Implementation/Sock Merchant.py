# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:20:39 2017

@author: User
"""

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

x = {i:0 for i in set(c)}

for i in c:
    x[i] += 1
    
print sum(map(lambda x:x//2, x.values()))
