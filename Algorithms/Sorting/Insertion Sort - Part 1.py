# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:38:39 2017

@author: User
"""

def insertionSort(ar):
    bm = ar[-1]
    for i in range(len(ar)-2,-1, -1):
        if ar[i] > bm:
            ar[i+1] = ar[i]
            print ' '.join(map(str, ar))
        else:
            ar[i+1] = bm
            bm = ar[i]
    ar[i] = bm
    print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)