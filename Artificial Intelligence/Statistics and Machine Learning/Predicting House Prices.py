# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:09:20 2017

@author: User
"""

from sklearn import linear_model
m, n = map(int, input().split())
X = [[0 for i in range(m)] for i in range(n)] 
Y = []
for i in range(n):
    row = list(map(float, input().split()))
    Y.append(row[-1]) 
    for k in range(m):
        X[i][k] = row[k]
        
q = int(input())
Q = [[0 for i in range(m)] for i in range(q)]

for i in range(q):
    row = list(map(float, input().split()))
    for v in range(m):
        Q[i][v] = row[v]
lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_


for i in range(q):
    ans = a
    for k in range(m):
        ans += Q[i][k] * b[k]
    print(round(ans, 2))   