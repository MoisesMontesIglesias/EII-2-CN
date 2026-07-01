#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QR decomposition
"""
import numpy as np
np.set_printoptions(suppress = True, precision=2)

def norm(v):
    return np.sqrt(np.sum(v**2))

def prod(u,v):
    return np.sum(u*v)

def proj(q,a):
    return prod(q,a)/prod(q,q)*q

def normaliza(v):
    return v/norm(v)

def Gram_Schmidt(A,p=False):
    Q = np.zeros_like(A)
    
    # Ortogonaliza
    for i in range(len(Q)):
        Q[:,i] = A[:,i]
        for j in range(i):
            Q[:,i] = Q[:,i] - proj(Q[:,j],A[:,i])
            
    if p == True:
        print('Q1 antes de normalizar')
        print(Q)  
        print('\n')
    
    # Normaliza        
    for i in range(len(Q)):
        Q[:,i] = normaliza(Q[:,i])        
        
    return Q    

def QR(A,p=False):
    Q = Gram_Schmidt(A,p)
    R = np.dot(Q.T,A)
    return Q , R
#%%---------------------------------------------------------------------------
print('----------------------  DATOS  ----------------------')
np.random.seed(3)  
n = 4
u1 = np.random.rand(n) - 0.5
v1 = np.random.rand(n) - 0.5
A1 = np.random.rand(n,n) 
print('u1 = ', u1) 
print('v1 = ', v1) 
print('A1 =')
print(A1)

print('\n')

n = 7
u2 = np.random.rand(n) 
v2 = np.random.rand(n)
A2 = np.random.rand(n,n)
print('u2 = ', u2) 
print('v2 = ', v2)  
print('A2 =')
print(A2)
#%%---------------------------------------------------------------------------
print('\n----------------------  EJERCICIO 1  ----------------------\n')
print('u1 . v1 = ', prod(u1,v1))
print('u2 . v2 = ', prod(u2,v2))
#%%---------------------------------------------------------------------------
print('\n----------------------  EJERCICIO 2  ----------------------\n')
print('norm(u1) = ', norm(u1))
print('norm(v2) = ', norm(v2))
#%%---------------------------------------------------------------------------
print('\n----------------------  EJERCICIO 3  ----------------------\n')
print('proj(u1,v1) = ', proj(u1,v1) )
print('proj(v2,u2) = ', proj(v2,u2) )
#%%---------------------------------------------------------------------------
print('\n----------------------  EJERCICIO 4  ----------------------\n')
print('normaliza(u1) = ', normaliza(u1) )
print('normaliza(v2) = ', normaliza(v2) )

#%%---------------------------------------------------------------------------
print('\n--------------------  EJERCICIOS 5 y 6  --------------------\n')
Q1, R1 = QR(A1,p=True)
print('Q1')
print(Q1)
print('R1')
print(R1)
print('\n')

Q2, R2 = QR(A2)
print('Q2')
print(Q2)
print('R2')
print(R2)
print('\n')


