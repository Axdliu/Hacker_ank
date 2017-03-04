# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:46:47 2017

@author: User
"""

import sys

def trade(price):
    n = len(price)
    share, cost, profit = 0, 0, 0
    top = price.index(max(price))
    while price != []:
        # print price
        share = len(price[:top])
        cost = sum(price[:top])
        profit += price[top]*share-cost
        if top < len(price) - 1:
            price = price[top+1:]
            top = price.index(max(price))
        else:
            break
    return profit

t = int(raw_input().strip())
for a0 in xrange(t):
    N = int(raw_input().strip())
    prices = map(int, raw_input().strip().split(' '))
    print trade(prices)