# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:29:24 2017

@author: User
"""

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)