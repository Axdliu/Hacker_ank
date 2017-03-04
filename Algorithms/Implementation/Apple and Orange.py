# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:17:10 2017

@author: User
"""

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

apple_d = [a+i for i in apple]
orange_d = [b+i for i in orange]
print len([i for i in apple_d if i>=s and i<=t])
print len([i for i in orange_d if i>=s and i<=t])
