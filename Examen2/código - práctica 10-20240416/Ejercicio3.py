# -*- coding: utf-8 -*-
"""
relajacion
"""
import numpy as np


#%%---------------------------------------------- 
def relajacion(A,b,w,tol,maxiter=1000):
    x    = np.zeros_like(b)
    xant = np.zeros_like(b)
    n = b.shape[0]
    k = 0
    while k < maxiter:
        for i in range(n):
    
            x[i]  = b[i]
    
            x[i] -= np.sum(A[i,:i]*x[:i])
    
            x[i] -= np.sum(A[i,i+1:]*xant[i+1:])
        
            x[i] *= w/A[i,i]
            
            x[i] += (1.- w)*xant[i]
            
        if np.linalg.norm(x-xant) < tol:
            k += 1
            break
        #pprint.pprint(x)    
        xant = x.copy()
        k += 1
    return x, k   

#%%----------------------------------------------
n = 9 

A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 

b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1.

tol = 1.e-6
w = 1.5

x, num_iter = relajacion(A,b,w,tol)

print('\n------------- Sistema 2 -------------')
print('\n', num_iter,' iteraciones')
print('\nx aproximada ')
print(x)    

xs = np.linalg.solve(A,b)
print('\nx exacta ')
print(xs)