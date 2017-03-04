# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:44:24 2017

@author: User
"""


n, k = map(int, raw_input().strip().split())

key_contests = []
counter = 0

for i in range(n):
    luck, importance = map(int, raw_input().strip().split())
    if importance == 1:
        key_contests.append(luck)
    counter += luck
#print counter, k, key_contests

if len(key_contests) <= k:
    print counter
else:
    counter = counter - 2*sum(sorted(key_contests,reverse=1)[k:])
    print counter
