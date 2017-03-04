# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 20:35:59 2017

@author: User
"""

def number_needed(a, b):
    counter = 0
    ful = a+b
    set_ful = set(ful)
    book = {i:0 for i in set_ful}
    for i in a:
        book[i] += 1
    for j in b:
        book[j] -= 1
    counter = sum(map(abs, book.values()))
    return counter

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)