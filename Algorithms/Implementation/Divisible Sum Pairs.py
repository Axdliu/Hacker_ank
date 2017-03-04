# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:19:07 2017

@author: User
"""

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

counter = 0
for i in xrange(n-1):
    for j in xrange(i+1,n):
        if (a[i]+a[j])%k == 0:
            # print i, j
            counter += 1
            
print counter