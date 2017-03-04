# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:02:10 2017

@author: User
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.len = len(self.name)
    def __repr__(self):
        return 'Point(name=%s, score=%s)' % (self.name, self.score)
    def comparator(a,b):        
        if a.score != b.score:
            return b.score - a.score
        else:
            for i in range(min(a.len, b.len)):
                if ord(a.name[i]) != ord(b.name[i]):
                    return ord(a.name[i]) - ord(b.name[i])
            return a.len - b.len