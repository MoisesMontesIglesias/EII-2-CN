#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ruffini
"""
import numpy as np
from Ejercicio1 import horner
from Ejercicio4 import divisores
   
#%%   
def raices(p):
    n = len(p)
    m = p[0]
    div = divisores(m)
    
    r = np.zeros(n-1)
    cont = 0
    for i in range(len(div)):
        resto = 0
        while resto == 0 and cont < n:
            cociente, resto = horner(div[i],p)
            if resto == 0:
                r[cont] = div[i]
                p = cociente
                cont += 1 
    return r            
#%%   

#(x-1)^3(x+2)(x-4)
p1 = np.array([8., -22, 17, 1, -5, 1])
print('\nRaíces de p1\n')
print(raices(p1))

#(x-1)^2(x-3)^3(x+5)
p2 = np.array([-135., 378, -369, 140, -9, -6, 1])
print('\nRaíces de p2\n')
print(raices(p2))

#(x-4)^2(x+1)^3(x+3) 
p3 = np.array([96.,320,366,135,-30,-24,0,1])    
print('\nRaíces de p3\n')
print(raices(p3))

#(x+1)^2(x-2)^3(x+5)(x-7)
p4 = np.array([280.,156,-350,-59,148,-26,-6,1])
print('\nRaíces de p4\n')
print(raices(p4))
#%%

