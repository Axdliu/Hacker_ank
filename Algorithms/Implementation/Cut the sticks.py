# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:27:41 2017

@author: User
"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

book = sorted(list(set(arr)))

for i in book:
    print n
    n -= arr.count(i)