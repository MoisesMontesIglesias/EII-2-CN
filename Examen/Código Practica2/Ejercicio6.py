#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
McLaurin
"""
import numpy as np         
import matplotlib.pyplot as plt


def funTanh(x,tol):
    
    fact1 = 1
    fact2 = 1
    
    co = 0.
    si = 0.
    tant = np.inf
    
    error = 1.
    k = 0
    
    while error > tol:
    
        co += x**(2*k)/fact1
        si += x**(2*k+1)/fact2
        t = si/co
        
        error = np.max(abs(t-tant))
        tant = t
        
        k += 1
        fact1 *= 2*k * (2*k-1)
        fact2 *= (2*k+1) * 2*k
    return t

f = lambda x: np.tanh(x)
tol = 1.e-8
x = np.linspace(-3,3)
y = funTanh(x, tol)

plt.figure()
plt.plot(x,f(x),'y', linewidth = 4,label = 'f')
plt.plot(x,y,'b--',label = 'Aproximación f')
plt.plot(x,x*0,'k')    
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()
