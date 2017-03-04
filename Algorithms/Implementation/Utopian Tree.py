# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:21:09 2017

@author: User
"""

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    for i in xrange(1, n+1):
        if i%2 == 1:
            h *= 2
        else:
            h += 1
    print h