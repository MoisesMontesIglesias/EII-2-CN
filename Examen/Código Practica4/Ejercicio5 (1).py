#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara tiempos de ejecución
"""
import numpy as np
import time
#%%   
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
#-----------------------------------------------------------    
A = np.array([[-3,2],[-2,0],[-4,4],[4,-4]])
B = np.array([[4,-3,1],[-2,1,1]])
C = multiplica_2blucles(A,B)

print('\nC\n', C)    
#-----------------------------------------------------------  
A1 = np.array([[-3,2],[-2,0],[-4,4],[4,-4],[1,1]])
B1 = np.array([[4,-3,1,1],[-2,1,1,1]])
C1 = multiplica_2blucles(A1,B1)
print('\nC1\n', C1)


