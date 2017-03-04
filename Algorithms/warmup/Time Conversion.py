# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:14:26 2017

@author: User
"""

import sys


time = raw_input().strip()

if time[8:] == 'PM':
    if int(time[0:2]) == 12:
        print time[0:8]
    else:
        print str(int(time[0:2])+12)+time[2:8]
else:
    if int(time[0:2]) == 12:
        print "00"+time[2:8]
    else:
        print time[0:8]