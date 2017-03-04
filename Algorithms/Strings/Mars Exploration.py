# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:35:44 2017

@author: User
"""

import sys
import itertools

S = raw_input().strip()

n = len(S)/3
mod = itertools.cycle('SOS')

counter = 0
for i in S:
    k = mod.next()
    if i != k:
        counter += 1
print counter