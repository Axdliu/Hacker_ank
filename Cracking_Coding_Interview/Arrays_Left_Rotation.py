# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 20:32:18 2017

@author: User
"""

def array_left_rotation(a, n, k):
    new = a[k:] + a[:k]
    return new
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
