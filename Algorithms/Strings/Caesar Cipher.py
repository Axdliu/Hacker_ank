# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:35:13 2017

@author: User
"""

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
new = ''
for i in s:
    if i.islower() or i.isupper():
        if ord(i) <= 90 and ord(i) + k > 90:
            new += chr((ord(i) + k - ord('A'))%26+ord('A'))
        elif ord(i) <= 122 and ord(i) + k > 122:
            new += chr((ord(i) + k - ord('a'))%26+ord('a'))
        else:
            new += chr(ord(i) + k)
    else:
        new += i
print new