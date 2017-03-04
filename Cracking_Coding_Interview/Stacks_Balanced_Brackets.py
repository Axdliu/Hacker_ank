# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 21:53:49 2017

@author: User
"""

def is_matched(expression):
    
    match = {'{':'}', '[':']', '(':')'}
    
    if expression[0] in match.values() or expression[-1] in match.keys():
        return 0
      
    pre = [expression[0]]
    
    for i in expression[1:]:
        try:
            testing = match[i]
            pre.append(i)
        except:
            if pre == []:
                return 0
            else:
                if i == match[pre[-1]]:
                    pre.pop()
                else:
                    return 0
    if pre == []:
        return 1
    else:
        return 0

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"