# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:10:39 2017

@author: User
"""

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]
a_s = 0
b_s = 0
for i in range(len(a)):
    if a[i] > b[i]:
        a_s += 1
    elif a[i] < b[i]:
        b_s += 1
print a_s, b_s