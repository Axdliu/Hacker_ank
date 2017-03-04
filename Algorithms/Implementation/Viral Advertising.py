# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:23:23 2017

@author: User
"""

days = int(raw_input())
n = 5
like = 5//2
last = like
for i in range(days-1):
    new = last*3//2
    like += new
    last = new
print like