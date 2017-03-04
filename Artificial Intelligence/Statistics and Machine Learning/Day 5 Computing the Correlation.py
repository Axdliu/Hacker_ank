# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:15:32 2017

@author: User
"""

n = int(raw_input())
data, M, P, C = [], [], [], []

for i in range(n):
    data = (map(float, raw_input().strip().split()))
    M.append(data[0])
    P.append(data[1])
    C.append(data[2])

def corr(A, B):
    n = len(A)
    u_A = sum(A)/n
    u_B = sum(B)/n
    var_A = 0
    var_B = 0
    cov = 0
    for i in xrange(n):
        var_A += (A[i]-u_A)**2
        var_B += (B[i]-u_B)**2
        cov += (A[i]-u_A)*(B[i]-u_B)
    return cov/(var_A*var_B)**0.5

print round(corr(M, P), 2)
print round(corr(C, P), 2)
print round(corr(M, C), 2)