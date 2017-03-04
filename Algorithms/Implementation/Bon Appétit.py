# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:20:11 2017

@author: User
"""

n, k = map(int, raw_input().strip().split(' '))
bill = map(int, raw_input().strip().split(' '))
charge = int(raw_input())

Anna = (sum(bill)-bill[k])/2
if Anna == charge:
    print 'Bon Appetit'
else:
    print charge-Anna