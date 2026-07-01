## module trapecio
# -*- coding: utf-8 -*-
"""
I = trapecio(f,a,b)
"""
import numpy as np
import sympy as sym
from Ejercicio1a import dibujo

def trapecio(f,a,b,plot=False):
    
    I = (b-a)*(f(a)+f(b))/2.;
    
    # Dibujo
    if plot == True:
        nodos = np.array([a,b])
        dibujo(f,a,b,nodos)
    
    return I
#-----------------------
def main():
    x = sym.Symbol('x', real=True) 
    f = sym.log(x)
    I_exacta = sym.integrate(f,(x,1,3))
    I_exacta = float(I_exacta)
    
    #-----------------------
    f = lambda x : np.log(x)
    a = 1.; b = 3
    I = trapecio(f,a,b,plot=True)
    print ('El valor aproximado es', I )
    print ('El valor exacto es    ', I_exacta)
    
if __name__ == "__main__":
    main()        