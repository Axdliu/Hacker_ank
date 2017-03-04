# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:43:30 2017

@author: User
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

N,l = map(int,raw_input().split())

UN = {str(i):0 for i in xrange(N)}
country_ID = 1

for i in xrange(l):
    a, b = raw_input().split()
    if UN[a] == 0 and UN[b] == 0:
        UN[a] = country_ID
        UN[b] = country_ID
        country_ID += 1
    elif UN[a] != 0 and UN[b] == 0:
        UN[b] = UN[a]
    elif UN[b] != 0 and UN[a] == 0:
        UN[a] = UN[b]
    else:
        max_c = max(UN[a], UN[b])
        min_c = min(UN[a], UN[b])
        for c in UN.keys():
            if UN[c] == max_c:
                UN[c] = min_c

UN_sum = UN.values()
UN_counter = sorted(list(set(UN_sum)))

unique = 0
if UN_counter[0] == 0:
    unique = UN_sum.count(0)
    UN_counter.pop(0)


staff_num = []
for i in UN_counter:
    staff_num.append(UN_sum.count(i))


# print unique, staff_num
comb = 0
for i in xrange(len(staff_num)-1):
    for j in xrange(i+1, len(staff_num)):
      comb += staff_num[i]*staff_num[j]  

print unique*(unique-1)/2+unique*sum(staff_num)+comb