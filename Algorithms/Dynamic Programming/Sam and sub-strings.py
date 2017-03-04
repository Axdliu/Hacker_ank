# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:45:06 2017

@author: User
"""

s=raw_input()
len1=len(s)
mul_ten=1
sum1=1
total_sum=len1*int(s[len1-1])
for i in range(len1-2,-1,-1):
    mul_ten=(mul_ten*10)%1000000007
    sum1=sum1+mul_ten
    total_sum=(total_sum+(sum1*(i+1))*int(s[i]))%1000000007
print total_sum%1000000007