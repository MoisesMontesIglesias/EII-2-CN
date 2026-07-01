## module Vandermonde
# -*- coding: utf-8 -*-
"""
V = Vandermonde(x,k)
Calcula la matriz de Vandermonde para los puntos
contenidos en el vector x
"""

def Vandermonde(x,k):
    
    import numpy as np    
    
    k = k+1
    n = len(x)
    V = np.empty(shape = (n,k))
    for i in range(n):
        for j in range(k):
            V[i,j] = x[i]**j
    
    return V