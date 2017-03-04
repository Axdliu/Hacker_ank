# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:39:08 2017

@author: User
"""

def insertionSort(ar):
    n = len(ar)
    for i in range(1, n):
        for j in range(i):
            if ar[j] > ar[i]:
                ar[j], ar[i] = ar[i], ar[j]
        print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)