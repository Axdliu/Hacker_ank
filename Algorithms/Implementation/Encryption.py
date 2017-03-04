# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:29:56 2017

@author: User
"""

import sys


s = raw_input().strip()

s = ''.join(s.split())

n = len(s)
row = int(n**0.5)
if n == row*row:
    column = row
else:
    column = row+1
    
if row*column < n:
    row += 1
    
s += (row*column-n)*' '

new_str = ''
for j in xrange(column):
    for i in xrange(row):
        new_str += s[i*column+j]
    new_str += ' '
print ' '.join(new_str.strip().split())  