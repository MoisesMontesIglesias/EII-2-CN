## module gauss
# -*- coding: utf-8 -*-
"""
V = gauss(f,a,b,n)
"""
import numpy as np
import sympy as sym
from Ejercicio1a import dibujo

def gauss(f,a,b,n):
    
    [x, w] = np.polynomial.legendre.leggauss(n)

    y = (b-a)/2*x+(b+a)/2
    I = sum(w*f(y))*(b-a)/2
   
    # Dibujo
    dibujo(f,a,b,y)
    
    
    return I
#-----------------------

x = sym.Symbol('x', real=True) 
f = sym.log(x)
I_exacta = sym.integrate(f,(x,1,3))
I_exacta = float(I_exacta)

#-----------------------
f = lambda x : np.log(x)
a = 1.; b = 3; n = 1
I = gauss(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)
#-----------------------
n = 2
I = gauss(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)
#-----------------------
n = 3
I = gauss(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)
#-----------------------