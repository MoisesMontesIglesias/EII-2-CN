#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara tiempos de ejecución
"""
import numpy as np
import time
#%%   
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

#-----------------------------------------------------------    
A = np.array([[-3,2],[-2,0],[-4,4],[4,-4]])
B = np.array([[4,-3,1],[-2,1,1]])
C = multiplica_1blucle(A,B)

print('\nC\n', C)    
#-----------------------------------------------------------  
A1 = np.array([[-3,2],[-2,0],[-4,4],[4,-4],[1,1]])
B1 = np.array([[4,-3,1,1],[-2,1,1,1]])
C1 = multiplica_1blucle(A1,B1)
print('\nC1\n', C1)


