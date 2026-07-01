#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara tiempos de ejecución
"""
import numpy as np
import time
#%%   
#-----------------------------------------------------
def multiplica_3blucles(A,B):
    m, n1 = A.shape
    n2, p = B.shape
    
    if n1 == n2:
        n = n1
    else:
        print('Error: las matrices deberían tener la misma dimensión intermedia')
        return
    
    C = np.zeros((m,p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i,j] += A[i,k]*B[k,j]
                
    return C   
#-----------------------------------------------------
def multiplica_2blucles(A,B):
    m, n1 = A.shape
    n2, p = B.shape
    
    if n1 != n2:
        print('Error: las matrices deberían tener la misma dimensión intermedia')
        return
    
    C = np.zeros((m,p))
    for i in range(m):
        for j in range(p):
            C[i,j] = np.sum(A[i,:]*B[:,j])
                
    return C 
#---------------------------------------------------
def multiplica_1blucle(A,B):
    m, n1 = A.shape
    n2, p = B.shape
    
    if n1 != n2:
        print('Error: las matrices deberían tener la misma dimensión intermedia')
        return
    
    C = np.zeros((m,p))
    for j in range(p):
        C[:,j] = np.sum(A*B[:,j],axis=1)
                
    return C 
#---------------------------------------------------

m = 300; n = 200; p = 400
A = np.random.rand(m,n)
B = np.random.rand(n,p)

t = time.time()  
print('Tiempo de ejecución con tres bucles')   
C = multiplica_3blucles(A,B)
print(time.time()-t)

t = time.time()  
print('Tiempo de ejecución con dos bucles')  
C = multiplica_2blucles(A,B)
print(time.time()-t)

t = time.time()  
print('Tiempo de ejecución con un bucle')  
C = multiplica_1blucle(A,B)
print(time.time()-t)

t = time.time()  
print('Tiempo de ejecución con el comando dot')  
C = np.dot(A,B)
print(time.time()-t)


