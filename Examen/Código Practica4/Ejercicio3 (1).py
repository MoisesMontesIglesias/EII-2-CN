#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
triangularización
"""
import numpy as np
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial
#------------------------------------
def triangulariza(Ar,b):
    n = len(b)
    At = np.copy(Ar)
    bt = np.copy(b)
    for k in range(n-1):
        f = At[k+1,0]/At[k,1]
        At[k+1,0] = 0.
        At[k+1,1] -= f*At[k,2] 
        bt[k+1] -= f*bt[k]
    return At,bt
#------------------------------------  
def sust_rev(At,bt):
    n = len(bt)
    x = np.zeros(n)
    x[n-1] = bt[n-1]/At[n-1,1]
    for k in range(n-2,-1,-1):
        x[k] = (bt[k]-At[k,2]*x[k+1])/At[k,1]
    return x    
#%%------------------------------------  
n = 7 

Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*3
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))

b = np.arange(n,2*n)*1.

print('-------------  DATOS  -------------')
print('Ar')
print(Ar)
print('b') 
print(b)
print('\n')
 
At, bt = triangulariza(Ar,b)
print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('\n')

print('------------ SOLUCIÓN ------------')
x = sust_rev(At,bt)

print('x')
print(x)
print('\n')
print('\n')
#%%------------------------------------ 
n = 8

np.random.seed(3)
Ar = np.zeros((n,3))
Ar[:,1] = np.random.rand(n)
Ar[:,0] = np.concatenate((np.array([0]),np.random.rand(n-1)))
Ar[0:n-1,2] = Ar[1:n,0]

b = np.random.rand(n)

print('-------------  DATOS  -------------')
print('Ar')
print(Ar)
print('b') 
print(b)
print('\n')
 
At, bt = triangulariza(Ar,b)
print('----  SISTEMA TRIANGULARIZADO ----')
print('At')
print(At)
print('\n')
print('------------ SOLUCIÓN ------------')
x = sust_rev(At,bt)

print('x')
print(x)


  
 
    
    
    
    
    