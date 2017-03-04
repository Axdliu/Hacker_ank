# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 20:44:47 2017

@author: User
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    dict = {}
    while head != None:
        if head in dict.keys():
            return 1
        dict[head] = 1
        head = head.next
    return 0 