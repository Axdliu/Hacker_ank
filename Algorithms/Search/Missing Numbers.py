# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:41:49 2017

@author: User
"""

n1 = int(raw_input())
s1 = raw_input().strip().split()
n2 = int(raw_input())
s2 = raw_input().strip().split()

sall = s1+s2
set1 = set(s1)
set2 = set(s2)
setall = sorted(set(sall))
book1, book2 = {i:0 for i in setall}, {i:0 for i in setall}

for i in s1:
    book1[i] += 1
for i in s2:
    book2[i] += 1
    
result = ''    
for i in setall:
    if book1[i] != book2[i]:
        result += (i+' ')

print result.strip()