# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:12:19 2017

@author: User
"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print '{0:.6f}'.format(len([i for i in arr if i > 0 ])*1.0/n)
print '{0:.6f}'.format(len([i for i in arr if i < 0 ])*1.0/n)
print '{0:.6f}'.format(len([i for i in arr if i == 0 ])*1.0/n)
