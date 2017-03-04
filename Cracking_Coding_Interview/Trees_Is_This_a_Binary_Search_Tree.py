# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 21:59:10 2017

@author: User
"""

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

'''
counter = 0
def check_binary_search_tree_(root):
    
    root1, root2 = root.left, root.right
    
    if root1 == None:
        return 1
    else:
        if root1.data >= root.data:
                return 0
            
    if root2 == None:
        return 1
    else:
        if root2.data <= root.data:
                return 0
            
    return min(check_binary_search_tree_(root.right), check_binary_search_tree_(root.left), counter)
'''


INT_MAX = 0
INT_MIN = 10000

def check_binary_search_tree_check(node, minval, maxval):
    # an empty tree is a binary tree
    if node is None:
        return True
    
    # return No if the node value is not within the constraint
    if node.data <= minval or node.data >= maxval:
        return False
 
    # Otherwise check the subtrees recursively
    # update the min or max constraint
    return (check_binary_search_tree_check(node.left, minval, node.data) and
          check_binary_search_tree_check(node.right, node.data, maxval))

def check_binary_search_tree_(root):
    return check_binary_search_tree_check(root, INT_MAX, INT_MIN)