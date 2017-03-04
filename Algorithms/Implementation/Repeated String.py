# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:27:53 2017

@author: User
"""

s = raw_input().strip()
n = long(raw_input().strip())
counter = 0
mod = n%len(s)
times = n//len(s)
full = s.count('a')
part = s[:mod].count('a')
print full*times+part
