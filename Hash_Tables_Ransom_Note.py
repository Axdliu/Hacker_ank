# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 20:49:56 2017

@author: User
"""

def ransom_note(magazine, ransom):
    book = {i:0 for i in set(magazine)}
    for j in magazine:
        book[j] += 1
    for k in ransom:
        try:
            book[k] -= 1
            #print book, book[k]
            if book[k] < 0:
                return 0
        except:
            return 0
    return 1

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"