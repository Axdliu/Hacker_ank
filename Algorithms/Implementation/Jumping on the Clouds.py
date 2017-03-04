# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:28:25 2017

@author: User
"""

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

mines = c.count(1)
safe = 0
jump = 0
m = 0
for i in c:
    m += 1

    if i == 0:
        safe += 1
    else:
        if safe >= 3:
            jump += (safe-1)//2
        safe = 0
if m == n:
    jump += (safe-1)//2
print n-1-mines-jump