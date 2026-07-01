## module simpson
# -*- coding: utf-8 -*-
"""
I = simpson(f,a,b)
"""
import numpy as np
import sympy as sym
from Ejercicio1a import dibujo

def simpson(f,a,b,plot=False):
    
    xm = (a+b)/2
    I = (b-a)*(f(a)+4*f(xm)+f(b))/6;

    # Dibujo
    if plot == True:
        nodos = np.array([a,xm,b])
        dibujo(f,a,b,nodos)
    
    return I
#-----------------------

x = sym.Symbol('x', real=True) 
f = sym.log(x)
I_exacta = sym.integrate(f,(x,1,3))
I_exacta = float(I_exacta)

#-----------------------
f = lambda x : np.log(x)
a = 1.; b = 3
I = simpson(f,a,b,plot=True)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)