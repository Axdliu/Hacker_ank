# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:58:55 2017

@author: User
"""

n, d = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))

print ' '.join(str(s) for s in (arr[d:] + arr[:d]))