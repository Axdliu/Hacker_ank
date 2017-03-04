# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 21:58:23 2017

@author: User
"""

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[0]
        
    def pop(self):
        self.first.pop()
        if self.second != []:
            self.first = [self.second.pop(0)]
        
    def put(self, value):
        if self.first == []:
            self.first = [value]
        else:
            self.second.append(value)   

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()