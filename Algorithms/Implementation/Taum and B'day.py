# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:29:56 2017

@author: User
"""

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    if x+z<y:
        print (x+z)*w + b*x
    elif y+z<x:
        print (y+z)*b + w*y
    else:
        print b*x + w*y