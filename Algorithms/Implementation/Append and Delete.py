# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:25:43 2017

@author: User
"""

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

len_s = len(s)
len_t = len(t)
stop = min(len_s, len_t)
left = stop
for i in range(stop):
    if s[i] != t[i]:
        left = i
        break
step = len_t-left+len_s-left
if k < step:
    print 'No'
elif k == step:
    print 'Yes'
else:
    if k>=(len_t+left):
        print 'Yes'
    elif (k-step)%2 == 0:
        print 'Yes'
    elif (k-step)>len_t*2:
        print 'Yes'
    else:
        print 'No'
    