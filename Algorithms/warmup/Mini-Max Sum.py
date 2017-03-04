# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:13:01 2017

@author: User
"""

a,b,c,d,e = raw_input().strip().split(' ')
num = [int(a),int(b),int(c),int(d),int(e)]
print sum(num)-max(num), sum(num)-min(num)