# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:47:07 2017

@author: User
"""

#!/usr/bin/py
def lonelyinteger(a):
    for i in set(a):
        if a.count(i) == 1:
            return i
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
