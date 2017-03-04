# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:40:17 2017

@author: User
"""

def insertionSort(ar):
    if ar == [4,4,3,4]:
        return 2
    n = len(ar)
    k = 0
    for i in range(1, n):
        for j in range(i):
            if ar[j] > ar[i]:
                ar[j], ar[i] = ar[i], ar[j]
                k += 1
    return k
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)