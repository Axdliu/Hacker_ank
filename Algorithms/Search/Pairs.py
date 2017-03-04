# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:42:29 2017

@author: User
"""

def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    book = {}
    answer = 0
    for i in a:  
        book[i] = 1
    for i in a:
        try:
            book[i+k]
            answer += 1
        except:
            continue
    return answer

# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)