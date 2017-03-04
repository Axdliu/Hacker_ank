# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:24:08 2017

@author: User
"""

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
for a0 in xrange(q):
    m = int(raw_input().strip())
    print (a[-(k%n):]+a[:-(k%n)])[m]