#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
triangularización
"""
import numpy as np
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial
#------------------------------------
def triangulariza(A,b):
    n = len(b)
    At = np.copy(A)
    bt = np.copy(b)
    for k in range(n-1):
        f = At[k+1,k]/At[k,k]
        At[k+1,k] = 0.
        At[k+1,k+1] -= f*At[k,k+1]
        bt[k+1] -= f*bt[k]
    return At,bt
#------------------------------------
n = 7

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T

b = np.arange(n,2*n)*1.

print('-------------  DATOS  -------------')
print('A')
print(A)
print('b')
print(b)
print('\n\n')

At, bt = triangulariza(A,b)

print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('bt')
print(bt)
print('\n\n')
#------------------------------------
n = 8

np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T

b = np.random.rand(n)

print('-------------  DATOS  -------------')
print('A')
print(A)
print('b')
print(b)
print('\n\n')

At, bt = triangulariza(A,b)

print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('bt')
print(bt)
print('\n\n')

for j in range(n):
            sign = (-1) ** j
            submatrix = [row[:j] + row[j+1:] for row in (matrix[1:])]
            det += sign * matrix[0][j] * determinant(submatrix)
        return det





