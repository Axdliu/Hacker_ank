# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:00:08 2017

@author: User
"""

def Insert(head, data):
    if head == None:
        return Node(data, None)
    else:
        if head.next == None:
            head.next = Node(data,None)
        else:
            Insert(head.next,data)
        return head
    