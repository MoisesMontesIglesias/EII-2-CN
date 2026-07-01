#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:09:22 2021

@author: esperanza
"""

import numpy as np
#from scipy.integrate import quad


def longitudArco(f,a,b,n):
    x = np.linspace(a,b,n+1)
    h = (b-a)/n
    df = np.zeros_like(x)
    for i in range(1,n):
        df[i] = (f(x[i+1])-f(x[i-1]))/(2*h)
    df[0] = (f(a+h)-f(a))/h
    df[-1] = (f(b)-f(b-h))/h    
    
    g = np.sqrt(1+df**2)
    
    suma = 0.
    for i in range(1,n):
        suma += g[i]
    inte = h/2*(g[0]+2*suma+g[-1])
    return inte

f = lambda x: np.log(1+x**2)
a = 0.
b = 2.
n = 1000
print(longitudArco(f,a,b,n))

f = lambda x: np.arctan(1+x**2)
a = -1.
b = 1.
n = 800

print(longitudArco(f,a,b,n))  

#gg = lambda x: np.sqrt(1+ (2*x/(1+x**2))**2)
#print(quad(gg,a,b)[0])  