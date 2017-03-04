# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:34:22 2017

@author: User
"""

s = set(list(reduce(lambda x,y:x+y, raw_input().strip().split()).lower()))


if len(s) == 26:
    print 'pangram'
else:
    print 'not pangram'