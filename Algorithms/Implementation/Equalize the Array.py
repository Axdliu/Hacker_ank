# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:28:54 2017

@author: User
"""


n = int(raw_input())

lists = map(int, raw_input().strip().split())

name = set(lists)
book = {k:0 for k in name}

for i in name:
    book[i] = lists.count(i)

# print book
print n-max(book.values())
    