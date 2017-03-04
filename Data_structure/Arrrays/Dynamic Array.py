# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:57:37 2017

@author: User
"""

seqList = []
query = []
lastAns = 0

N, n_query = map(int, raw_input().split())

for i in range(N):
    seqList.append([])

for line in sys.stdin:
    query.append( list( map(int, line.split()) ) )

for i in query:
    seq = seqList[(i[1]^lastAns)%N]
    if i[0] == 1:
        seq.append(i[2])
    else:
        lastAns = seq[i[2]%len(seq)]
        print lastAns