## module punto_medio
# -*- coding: utf-8 -*-
"""
V = punto_medio(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import numpy.polynomial.polynomial as pol

def dibujo(f,a,b,nodos):
    plt.figure()
    ## Área exacta (function: blue 'b')
    # Top: function
    xp = np.linspace(a,b) # 50  points
    plt.plot(xp,f(xp),'b',label = 'Área exacta')
    # Closure
    plt.plot([a,a,b,b],[f(a),0,0,f(b)],'b')
    
    # Interpolation points (red points: 'ro')
    plt.plot(nodos,f(nodos),'ro',label = 'Puntos de interpolación')
    
    # Approximate area (red dashed line: 'r--')
    # interpolation polynomial
    p = pol.polyfit(nodos,f(nodos),len(nodos)-1)
    xp = np.linspace(a,b) # 50  points
    yp = pol.polyval(xp,p)
    plt.plot(xp,yp,'r--',label = 'Área aproximada')
    # closure
    pa = pol.polyval(a,p)
    pb = pol.polyval(b,p)
    plt.plot([a,a,b,b],[pa,0,0,pb],'r--')
    
    plt.legend()
    plt.show()

#%%-----------------------
def punto_medio(f,a,b,plot=False):
    
    xm = (a+b)/2
    I = (b-a) * f(xm) 
    
    # Dibujo
    if plot == True:
        nodos = np.array([xm])
        dibujo(f,a,b,nodos)
       
    return I
#%%-----------------------
def main():
    x = sym.Symbol('x', real=True) 
    f = sym.log(x)
    I_exacta = sym.integrate(f,(x,1,3))
    I_exacta = float(I_exacta)
    
    #-----------------------
    f = lambda x : np.log(x)
    a = 1.; b = 3
    I = punto_medio(f,a,b,plot=True)
    print ('El valor aproximado es', I )
    print ('El valor exacto es    ', I_exacta)
    

if __name__ == "__main__":
    main()    