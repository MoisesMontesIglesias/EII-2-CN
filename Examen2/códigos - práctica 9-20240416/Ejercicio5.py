#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integración montecarlo
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def montecarlo(f,a,b,n):
    
    x = np.linspace(a,b,n)
    M = max(f(x)) 
    m = min(f(x))
    np.random.seed(333)
    r = np.random.random((n,2))
    xx = r[:,0]*(b-a) + a
    yy = r[:,1]*(M-m) + m
    label = np.zeros_like(xx)
    pos = 0.
    neg = 0.
    for i in range(n):
        if f(xx[i]) > 0 and yy[i] > 0:
            if f(xx[i]) - yy[i] > 0:
                pos += 1.
                label[i] = 1
        if f(xx[i]) < 0 and yy[i] < 0: 
            if yy[i] - f(xx[i]) > 0:
                neg += 1.
                label[i] = 2          
    I  = float(pos)/float(n)
    I -= float(neg)/float(n)
    I *= (b-a)*(M-m)
    
    plt.plot(x,f(x),'b-')
    plt.plot(xx[label==0],yy[label==0],'ko',markersize = 1)
    plt.plot(xx[label==1],yy[label==1],'go',markersize = 1)
    plt.plot(xx[label==2],yy[label==2],'ro',markersize = 1)
        
    plt.plot(xx,0*xx,'k-')
    plt.plot([a,b,b,a,a],[m,m,M,M,m],'k-')
    plt.show()    
    return I        
        


#%%    
#-----------------------

x = sym.Symbol('x', real=True) 
f = 10*sym.exp(-x**2) - 6
I_exacta = sym.integrate(f,(x,-2,2))
I_exacta = float(I_exacta)

#%%-----------------------
f = lambda x : 10*np.exp(-x**2) - 6
a = -2.; b = 2.; n = 1000



I = montecarlo(f,a,b,n)
print ('El valor aproximado es %f' % (I))
print ('El valor exacto es     %f' % (I_exacta))