# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:25:31 2017

@author: User
"""

import sys


n = int(raw_input().strip())

fac = 1

for g in range(1, n+1):
    fac *= g
    
print fac