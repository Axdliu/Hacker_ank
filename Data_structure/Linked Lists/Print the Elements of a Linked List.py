# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:59:26 2017

@author: User
"""

def print_list(head):
    if head is not None:
        print(head.data)
        print_list(head.next)