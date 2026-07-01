#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gauss mod
"""
import numpy as np
np.set_printoptions(precision = 2)   
np.set_printoptions(suppress = True)
#%%
def triangular(A,b):
    At = np.copy(A)
    bt = np.copy(b)
    
    At[0,1] /= At[0,0]
    bt[0] /= At[0,0] 
    At[0,0] = 1.
    for k in range(1,n):
        At[k,k] -= At[k,k-1]*At[k-1,k]
        bt[k]   -= At[k,k-1] * bt[k-1]
        At[k,k-1]  = 0.
        
        if k < n-1:
            At[k,k+1] /= At[k,k]
        bt[k]   /= At[k,k]
        At[k,k]  = 1.
        
    return At, bt    
#%%
def back_subs(At,bt):

    x = np.zeros_like(bt)
    x[n-1] = bt[n-1]
    for k in range(n-2,-1,-1):
        x[k] = bt[k] - At[k,k+1] * x[k+1]
    
    return x    
    
#%%
print('-------------  DATOS 1  -------------')
n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.

print('A')
print(A)
print('b')
print(b)

print('\n-------  SISTEMA TRIANGULAR 1 -------') 
At1, bt1 = triangular(A,b)  
print('At1')
print(At1)
print('bt1')
print(bt1) 

#%%
print('\n-------  SOLUCIÓN 1 -------')  
x = back_subs(At1,bt1) 
print('x')
print(x)  

#%%
print('\n\n-------------  DATOS 2  -------------')
n = 8 

np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 

b = np.random.rand(n)

print('A')
print(A)
print('b')
print(b)

print('\n-------  SISTEMA TRIANGULAR 2 -------')  
At2, bt2 = triangular(A,b) 
print('At2')
print(At2)
print('bt2')
print(bt2) 
#%%    
print('\n-------  SOLUCIÓN 2 -------')   
x = back_subs(At2,bt2)
print('x')
print(x)    

