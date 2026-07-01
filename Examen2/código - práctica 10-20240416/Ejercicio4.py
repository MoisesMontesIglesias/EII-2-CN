# -*- coding: utf-8 -*-
"""
relajacion
"""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 7)   
np.set_printoptions(suppress = True)
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

tol = 1.e-12

w = np.arange(0.1,2.1,0.01)
num_iter = np.zeros(len(w))
for i in range(len(w)):
    x, num_iter[i] = relajacion(A,b,w[i],tol)
    
k = np.argmin(num_iter)    
print('Óptimo w = %.2f  num_iter = %i ' % (w[k],num_iter[k]))

plt.figure()
plt.plot(w,num_iter)    
plt.xlabel('w',fontsize=16)
plt.ylabel('iteraciones',fontsize=16)
plt.grid()
plt.axis([min(w),max(w),0,1050])
#plt.show()
