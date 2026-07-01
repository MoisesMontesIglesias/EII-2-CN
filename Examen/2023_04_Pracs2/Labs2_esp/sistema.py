# -*- coding: utf-8 -*-
"""
Gauss-Seidel con Matriz Tridiagonal
"""
import numpy as np
np.set_printoptions(precision = 3)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial  
#%%
def GaussSeidel(A,b,niter):
    x = np.zeros_like(b)
    
    n = len(b)
    for k in range(niter):
        x[0] = (b[0] - A[0,1]*x[1])/A[0,0]
        for i in range(n-1):
            x[i] = (b[i] - A[i,i-1]*x[i-1] - A[i,i+1]*x[i+1])/A[i,i]
        x[n-1] = (b[n-1] - A[n-1,n-2]*x[n-2])/A[n-1,n-1]
        print('\niter = ', k+1)
        print(x)       
#%%    
print('PRIMER SISTEMA')  
n = 7 
A1 = np.diag(np.ones(n))*4
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.

print('A')
print(A)
print('\nb')
print(b)

niter = 5
GaussSeidel(A,b,niter)
  
print('\nSolución exacta:')
print(np.linalg.solve(A,b))
#%%
print('\n\n')
print('SEGUNDO SISTEMA')  
n = 8 
np.random.seed(2)
A1 = np.diag(np.random.rand(n))*5
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 

b = np.random.rand(n)
print('A')
print(A)
print('\nb')
print(b)


niter = 4
GaussSeidel(A,b,niter)

print('\nSolución exacta:')
print(np.linalg.solve(A,b))

