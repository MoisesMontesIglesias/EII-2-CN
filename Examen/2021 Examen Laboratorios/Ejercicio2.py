#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:54:40 2021

@author: esperanza
"""

import numpy as np
np.set_printoptions(suppress=True,precision=2)



def factoriza(A):
    n,m = A.shape
    C = np.zeros_like(A)
    C[0,0] = np.sqrt(A[0,0])
    for k in range(1,n):
        C[k,k-1] = A[k,k-1]/C[k-1,k-1]
        C[k,k] = np.sqrt(A[k,k]-C[k,k-1]**2)
    return C

n = 7
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),-1)
A = A1 + A2 + A2.T
print(A)
C = factoriza(A)
print(np.dot(C,C.T))
print(C)  

np.random.seed(2)
n = 8
A1 = np.diag(np.random.rand(n))*10
A2 = np.diag(np.random.rand(n-1),-1)
A = A1 + A2 + A2.T
print(A)
C = factoriza(A)
print(np.dot(C,C.T))
print(C) 