# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:34:23 2017

@author: User
"""

import sys

c = 0
s = raw_input().strip()

for l in s:
    if l.isupper():
        c += 1
        
print c+1