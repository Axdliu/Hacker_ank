# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:26:56 2017

@author: User
"""

ret = map(int, raw_input().strip().split())
due = map(int, raw_input().strip().split())

def fine(ret, due):
    if ret[2]<due[2]:
        return 0
    elif ret[2]==due[2]:
        if ret[1]<due[1]:
            return 0
        elif ret[1]==due[1]:
            if ret[0]<=due[0]:
                return 0
            else:
                return (ret[0]-due[0])*15
        else:
            return (ret[1]-due[1])*500
    else:
        return 10000

print fine(ret, due)