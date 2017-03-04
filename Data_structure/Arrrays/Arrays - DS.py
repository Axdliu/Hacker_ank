# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:48:00 2017

@author: User
"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print " ".join([str(x) for x in arr[::-1]])