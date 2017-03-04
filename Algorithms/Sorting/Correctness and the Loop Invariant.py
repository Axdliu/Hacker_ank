# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:39:35 2017

@author: User
"""

def insertion_sort(ar):
    n = len(ar)
    for i in range(1, n):
        for j in range(i):
            if ar[j] > ar[i]:
                ar[j], ar[i] = ar[i], ar[j]
    return ar


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))