#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:43:33 2021

@author: esperanza
"""

import numpy as np
import matplotlib.pyplot as plt

def optim(f,a,b,n):
    x = np.linspace(a,b,n)
    maxi = np.zeros(n)
    mini = np.zeros(n)
    k1 = 0
    k2 = 0
    for i in range(1,n-1):
        if f(x[i])> f(x[i-1]) and f(x[i])> f(x[i+1]):
            maxi[k1] = x[i]
            k1 += 1
        if f(x[i])< f(x[i-1]) and f(x[i])< f(x[i+1]):
            mini[k2] = x[i]
            k2 += 1 
    
    maxi = maxi[:k1]
    mini = mini[:k2]
    return maxi,mini

def pinta(f,a,b,maxi,mini):
    x = np.linspace(a,b)
    plt.figure()
    plt.plot(x,f(x))
    plt.plot(maxi,f(maxi),'ro')
    plt.plot(mini,f(mini),'bo')
    plt.show()
   
a = -2.
b = 2.
n = 1000
f = lambda x: x**2 + np.log(x+5)*np.cos(3*x)

maxi,mini = optim(f,a,b,n)
print(maxi)
print(mini)  
pinta(f,a,b,maxi,mini)

a = 0.
b = 2.
n = 500
f = lambda x: x**2 * np.sin(6*x)

maxi,mini = optim(f,a,b,n)
print(maxi)
print(mini)  
pinta(f,a,b,maxi,mini)












 