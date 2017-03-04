# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:15:20 2017

@author: User
"""

import sys
import string

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()

strings = ''.join(word.split(' '))
codebook = dict((n,v) for (n,v) in zip([i for i in string.lowercase[:]],h))
print len(strings)*max([codebook[i] for i in strings])
