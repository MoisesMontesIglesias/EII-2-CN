#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derivadas sucesivas
"""
import numpy as np
import matplotlib.pyplot as plt
from Ejercicio1 import horner
#%%
def derivadasSuc(p,x):
    m = len(x)
    n = len(p)
    derivadas = np.zeros((m,n))
    for k in range(m):
        x0 = x[k]
        factorial = 1.       
        c, r = horner(x0,p)       
        derivadas[k,0] = r
        for i in range(1,n):
            factorial *= i
            c, r = horner(x0,c)
            derivadas[k,i] = r*factorial
    return derivadas        
#%%
p = np.array([1., -1, 2, -3, 5, -2])

x = np.linspace(0,1)

derivadas = derivadasSuc(p,x)  

plt.plot(x,x*0,'k')
plt.plot(x,derivadas[:,0], label=r'$P$')
plt.plot(x,derivadas[:,1], label=r'$P^{\prime}$')
plt.plot(x,derivadas[:,2], label=r'$P^{\prime\prime}$')
plt.legend()
#plt.show()
 
