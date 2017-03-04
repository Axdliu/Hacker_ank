# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:25:01 2017

@author: User
"""

import sys


t = int(raw_input().strip())



for a0 in xrange(t):
    counter = 0
    n = raw_input().strip()
    for d in n:
        if int(d) != 0:
            if int(n)%int(d) == 0:
                counter += 1
    print counter
