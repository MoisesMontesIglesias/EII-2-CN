#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taylor
"""
import numpy as np         
import matplotlib.pyplot as plt     

x = np.pi/4

def funSen(x,tol,maxiter):
    fact = 1.

    si = 0.
    error = 1.
    k = 0
    signo = 1

    while error > 1.e-4 and k < maxiter:    

        term = x**(2*k+1)/fact
        si += term*signo


        error = np.max(abs(term))

        k += 1
        fact *= 2*k * (2*k+1)
        signo *= -1
    return si    
    
f = lambda x: np.sin(x)
tol = 1.e-8
maxiter = 100
x = np.linspace(-np.pi,np.pi)
y = funSen(x, tol, maxiter)

plt.figure()
plt.plot(x,f(x),'y', linewidth = 4,label = 'f')
plt.plot(x,y,'b--',label = 'Aproximación f')
plt.plot(x,x*0,'k')    
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show() 
