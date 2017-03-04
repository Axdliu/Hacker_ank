# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:31:37 2017

@author: User
"""

import math

n, k = map(int, raw_input().strip().split())
t = map(int, raw_input().strip().split())
page = 1
result = 0
content = 0
full = {}

for i in t:
    if content != 0:
        page += 1
        content = 0
    for j in range(1,i+1):
        content += 1
        if content == 1:
            full[page] = [j]
        else:
            full[page].append(j)
        if j == page:
            result += 1
        #    print j, page
        if content == k:
            page += 1
            content = 0
    
print result