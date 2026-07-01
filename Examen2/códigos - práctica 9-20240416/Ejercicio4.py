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
    m = 0.
    np.random.seed(11)
    r = np.random.random((n,2))
    xx = r[:,0]*(b-a) + a
    yy = r[:,1]*(M-m) + m
    label = np.zeros_like(xx)
    
    cont = sum(yy-f(xx) < 0)
    cc = np.where(yy-f(xx) < 0)[0]
    label[cc] = 1
           
    I = float(cont)/float(n)*(b-a)*(M-m) 
    
    plt.plot(x,f(x),'b-')
    plt.plot(xx[label==0],yy[label==0],'ko',markersize = 1)
    plt.plot(xx[label==1],yy[label==1],'ro',markersize = 1)
    plt.plot([a,b,b,a,a],[m,m,M,M,m],'k-')
    plt.show()    
    return I        
        


#%%    
#-----------------------

x = sym.Symbol('x', real=True) 
f = sym.exp(-x**2) 
I_exacta = sym.integrate(f,(x,-2,2))
I_exacta = float(I_exacta)

#-----------------------
f = lambda x : np.exp(-x**2)
a = -2.; b = 2.; n = 500



I = montecarlo(f,a,b,n)
print ('El valor aproximado es %f' % (I))
print ('El valor exacto es     %f' % (I_exacta))