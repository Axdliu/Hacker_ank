# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:46:26 2017

@author: User
"""

n0, n1, k = map(int, raw_input().strip().split())

for i in range(2,k):
    n2 = n0 + n1**2
    n0, n1 = n1, n2
print n2