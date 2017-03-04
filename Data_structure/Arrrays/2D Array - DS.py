# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:56:04 2017

@author: User
"""

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
    
answer = -9*7-1
case = 0
for i in range(4):
    for j in range(4):
        if (sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])) > answer:
            answer = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
print answer