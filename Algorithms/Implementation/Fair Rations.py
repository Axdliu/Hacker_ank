# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:32:00 2017

@author: User
"""

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

Bb = map(lambda x:x%2, B)

odd = Bb.count(1)

if odd%2 != 0:
    print 'NO'
else:
    counter = 0
    switch = 0
    for l in xrange(N):
        if Bb[l] == 1:
            switch = 1 - switch
            if switch == 1:
                start = l
            else:
                counter += l-start
    print counter*2