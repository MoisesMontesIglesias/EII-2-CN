#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
#%%---------------------------------------------- 
def jacobir(Ar,b,tol,maxiter=1000):
    x    = np.zeros_like(b)
    xant = np.zeros_like(b)
    n = b.shape[0]
    k = 0
    while k < maxiter:
        x[0]  = (b[0] - Ar[0,2]*xant[1])/Ar[0,1]
        for i in range(1,n-1):
    
            x[i]  = b[i]
    
            x[i] -= Ar[i,0]*xant[i-1]
    
            x[i] -= Ar[i,2]*xant[i+1]
    
            x[i] /= Ar[i,1]
            
        x[n-1]  = (b[n-1] - Ar[i,0]*xant[n-2])/Ar[n-1,1]
        
        if np.linalg.norm(x-xant) < tol:
            k += 1
            break
        xant = x.copy()
        k += 1
    return x, k 
#%%---------------------------------------------- 
def gauss_seidelr(A,b,tol,maxiter=1000):
    x    = np.zeros_like(b)
    xant = np.zeros_like(b)
    n = b.shape[0]
    k = 0
    while k < maxiter:
        x[0]  = (b[0] - Ar[0,2]*xant[1])/Ar[0,1]
        for i in range(1,n-1):
    
            x[i]  = b[i]
    
            x[i] -= Ar[i,0]*x[i-1]
    
            x[i] -= Ar[i,2]*xant[i+1]
    
            x[i] /= Ar[i,1]
            
        x[n-1]  = (b[n-1] - Ar[i,0]*x[n-2])/Ar[n-1,1]
        
        if np.linalg.norm(x-xant) < tol:
            k += 1
            break
        xant = x.copy()
        k += 1
    return x, k  
#%%---------------------------------------------- 
def relajacionr(A,b,w,tol,maxiter=1000):
    x    = np.zeros_like(b)
    xant = np.zeros_like(b)
    n = b.shape[0]
    k = 0
    while k < maxiter:
        x[0]  = (b[0] - Ar[0,2]*xant[1])/Ar[0,1] * w
        x[0] += (1.- w)*xant[0]
        for i in range(1,n-1):
    
            x[i]  = b[i]
    
            x[i] -= Ar[i,0]*x[i-1]
    
            x[i] -= Ar[i,2]*xant[i+1]
    
            x[i] /= Ar[i,1]
            
            x[i] *= w
            
            x[i] += (1.- w)*xant[i]
            
        x[n-1]  = (b[n-1] - Ar[i,0]*x[n-2])/Ar[n-1,1] * w
        x[n-1] += (1.- w)*xant[n-1]
        
        if np.linalg.norm(x-xant) < tol:
            k += 1
            break
        xant = x.copy()
        k += 1
    return x, k    
#%%---------------------------------------------- 
n = 9 

Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*2
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))

b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1.
tol = 1.e-6
w = 1.5
x1, num_iter1  = jacobir(Ar,b,tol)
x2, num_iter2  = gauss_seidelr(Ar,b,tol)
x3, num_iter3  = relajacionr(Ar,b,w,tol)
    
print('\n------------- Sistema 2 -------------')
print('\n          ---- Datos ----')
print('Ar')
print(Ar)
print('b') 
print(b)
print('\n          ---- Jacobi ----')
print('\n', num_iter1,' iteraciones')
print('\nx ')
print(x1)    
print('\n          ---- Gauss-Seidel ----')
print('\n', num_iter2,' iteraciones')
print('\nx ')
print(x2) 
print('\n          ---- Relajación ----')
print('\n', num_iter3,' iteraciones')
print('\nx ')
print(x3)
print('\n          ---- Solución exacta ----\n')
print('[0.5 0.  1.5 0.  2.5 0.  1.5 0.  0.5]')
