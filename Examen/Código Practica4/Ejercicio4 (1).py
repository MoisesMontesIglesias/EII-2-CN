#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multiplica matrices: 3 bucles
"""
import numpy as np

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
           
#-----------------------------------------------------------    
A = np.array([[-3,2],[-2,0],[-4,4],[4,-4]])
B = np.array([[4,-3,1],[-2,1,1]])
C = multiplica_3blucles(A,B)

print('\nC\n', C)    
#-----------------------------------------------------------  
A1 = np.array([[-3,2],[-2,0],[-4,4],[4,-4],[1,1]])
B1 = np.array([[4,-3,1,1],[-2,1,1,1]])
C1 = multiplica_3blucles(A1,B1)
print('\nC1\n', C1)

