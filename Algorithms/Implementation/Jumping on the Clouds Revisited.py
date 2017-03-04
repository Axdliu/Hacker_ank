# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:24:29 2017

@author: User
"""

import sys
import itertools

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

'''
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
'''
counter = 100
for i in range(n/k):
    if c[i*k] == 0:
        counter -= 1
    else:
        counter -= 3
print counter