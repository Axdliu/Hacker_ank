# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:00:51 2017

@author: User
"""

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

counter = 0

for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            counter += 1

print 'Array is sorted in', counter, 'swaps.'
print 'First Element:', a[0]
print 'Last Element:', a[-1]