# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:36:47 2017

@author: User
"""

import sys


n = int(raw_input().strip())
B = raw_input().strip()

last = None
index = []
temp = ''
for i in B:
    if last == None and i == '0':
        last = i
        temp += i
    elif last != None:
        if i != last:
            last = i
            temp += i
        else:
            index.append(temp)
            if i == '0':
                last = i
                temp = i
            else:    
                temp = ''
                last = None

index.append(temp)
output = sum(map(lambda x:(len(x)-3)//4+1, index))
print output   