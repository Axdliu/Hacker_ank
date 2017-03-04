# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:11:50 2017

@author: User
"""

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

gap = 0
for i in range(len(a)):
    gap += (a[i][i]-a[i][-i-1])
print abs(gap)