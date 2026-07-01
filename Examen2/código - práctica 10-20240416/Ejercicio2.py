# -*- coding: utf-8 -*-
"""

"""
import numpy as np


#%%---------------------------------------------- 
def gauss_seidel(A,b,tol,maxiter=1000):
    x    = np.zeros_like(b)
    xant = np.zeros_like(b)
    n = b.shape[0]
    k = 0
    while k < maxiter:
        for i in range(n):
    
            x[i]  = b[i]
    
            x[i] -= np.sum(A[i,:i]*x[:i])
    
            x[i] -= np.sum(A[i,i+1:]*xant[i+1:])
    
            x[i] = x[i]/A[i,i]
    
        if np.linalg.norm(x-xant) < tol:
            k += 1
            break
        xant = x.copy()
        k += 1
    return x, k   
#%%----------------------------------------------
A = np.array([[5.,1.,-1.,-1.],[1.,4.,-1.,1.],[1.,1.,-5.,-1.],[1.,1.,1.,-4.]])
b = np.array([1.,1.,1.,1.])
tol = 1.e-6

x, num_iter = gauss_seidel(A,b,tol)

print('\n------------- Sistema 1 -------------')        
print('\n', num_iter,' iteraciones')
print('\nx aproximada ')
print(x)    

xs = np.linalg.solve(A,b)
print('\nx exacta ')
print(xs)
#%%----------------------------------------------
n = 9 

A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 

b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1.

tol = 1.e-6

x, num_iter = gauss_seidel(A,b,tol)

print('\n------------- Sistema 2 -------------')
print('\n', num_iter,' iteraciones')
print('\nx aproximada ')
print(x)    

xs = np.linalg.solve(A,b)
print('\nx exacta ')
print(xs)