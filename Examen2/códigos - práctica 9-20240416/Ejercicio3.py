#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
grado de precision
"""
import numpy as np
import sympy as sym
from scipy.integrate import fixed_quad
#%%-------------------------------------------
def punto_medio(f,a,b):
    
    I = (b-a)*f((a+b)/2)
    return I
#%%-------------------------------------------
def trapecio(f,a,b):
    
    I = (b-a)*(f(a)+f(b))/2.;
    return I
#%%-------------------------------------------
def simpson(f,a,b):
    
    I = (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
    return I
#%%-------------------------------------------
def newton_cotes(f,a,b,n):
    if n == 1:
        I = punto_medio(f,a,b)
    elif n == 2:
        I = trapecio(f,a,b)
    elif n == 3:
        I = simpson(f,a,b)
    return I    
#%%-------------------------------------------
def gauss(f,a,b,n):
    
    [x, w] = np.polynomial.legendre.leggauss(n)

    y = (b-a)/2*x+(b+a)/2
    I = sum(w*f(y))*(b-a)/2
    return I
#%%-------------------------------------------
def grado_de_precision(formula,n):

    t = sym.Symbol('t', real=True) 
    
    a = 1.; b = 3;
    i = 0
    error = 0.
    
    while error < 1.e-11:
        p = lambda x: x**i
        p_s = t**i
        Ia = formula(p,a,b,n)
    
        I_exacta = float(sym.integrate(p_s,(t,1,3)))
        error = np.abs(Ia - I_exacta)
        print('f(x) = x^'+str(i), '  error = ',error)
        
        i += 1
    print('\nEl grado de precisión es '+str(i-2),'\n') 
#%%
print('\n----  Fórmula del punto medio (n = 1) ----\n')
grado_de_precision(newton_cotes,1)   
print('\n----  Fórmula del trapecio (n = 2) ----\n') 
grado_de_precision(newton_cotes,2)  
print('\n----  Fórmula de Simpson (n = 3) ----\n')   
grado_de_precision(newton_cotes,3)   
print('\n----  Fórmula Gauss n = 1  ----\n')  
grado_de_precision(gauss,1)    
print('\n----  Fórmula Gauss n = 2  ----\n')  
grado_de_precision(gauss,2)
print('\n----  Fórmula Gauss n = 3  ----\n')  
grado_de_precision(gauss,3) 
print('\n----  Fórmula Gauss n = 4  ----\n')  
grado_de_precision(gauss,4)  