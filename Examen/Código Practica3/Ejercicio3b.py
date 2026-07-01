#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derivadas sucesivas
"""
import numpy as np
from Ejercicio1 import horner
np.set_printoptions(suppress = True)
#%%
def dersuc(x0,p):
    derivadas = np.zeros_like(p)

    c = np.copy(p)
    factorial = 1.
    for k in range(len(c)):  
        c, r = horner(x0,c)
        derivadas[k] = r*factorial
        factorial *= k+1
    return derivadas    
#%%-------------------------------- 
#%%
p = np.array([1., -1, 2, -3,  5, -2])
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x0 = 1.
x1 = -1.

print('Derivadas sucesivas de P en x0 = 1')    
print(dersuc(x0,p)) 
print('\n')
print('Derivadas sucesivas de R en x1 = -1')
print(dersuc(x1,r))   
