# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:03:09 2017

@author: User
"""

def prime(n):    
    root = int(n**0.5)
    if n == 1:
        return 'Not prime'
    elif  root == n**0.5:
        return 'Not prime'
    else:
        for i in range(2, root+1):
            if n%i == 0:
                return 'Not prime'
        return 'Prime'
        


p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    print prime(n)