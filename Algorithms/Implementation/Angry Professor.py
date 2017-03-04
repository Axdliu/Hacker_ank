# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:21:47 2017

@author: User
"""

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))