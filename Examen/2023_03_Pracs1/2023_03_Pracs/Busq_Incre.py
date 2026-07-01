#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#%%
def busquedaIncremental(f,a,b,n):
    x = np.linspace(a,b,n+1)
    intervalos = np.zeros((n,2))
    contador = 0
    for i in range(n):
        if f(x[i])*f(x[i+1]) < 0:
            intervalos[contador] = x[i:i+2]
            contador +=1
    intervalos = intervalos[:contador]
    return intervalos
#%%
def raices(f,a,b,tol=1.e-4):
    
    n = int((b-a)/0.1)
    numiter = int(-np.log10(tol)-1)
    intervalos = busquedaIncremental(f,a,b,n)
    r = np.zeros(len(intervalos))
    
    for k in range(len(intervalos)):
        a0 = intervalos[k,0]
        b0 = intervalos[k,1]
        for i in range(numiter):
            intervalo1 = busquedaIncremental(f,a0,b0,10)
            a0 = intervalo1[0,0]
            b0 = intervalo1[0,1]
        r[k] = a0  
    
    # gráfica
    x = np.linspace(a,b)
    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.show()  
    
    return r 
#%%
np.set_printoptions(precision = 5) 
p = np.array([1., 0.2, -7., 0.7, 8])
f = lambda x: np.polyval(p,x)
a = -3
b = 2.5
tol = 1.e-5
r = raices(f,a,b,tol)
print(r)
   

#%%
np.set_printoptions(precision = 3) 
p = np.array([1., -0.3, -5.8, 3, 5, -2.6])
f = lambda x: np.polyval(p,x)
a = -2.5; b = 2.5
tol = 1.e-3
r = raices(f,a,b,tol)
print(r)
