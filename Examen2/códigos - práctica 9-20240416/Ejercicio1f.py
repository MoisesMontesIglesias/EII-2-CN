## module simpson_comp
# -*- coding: utf-8 -*-
"""
V = simpson_comp(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import numpy.polynomial.polynomial as pol


def simpson_comp(f,a,b,n):
    
    h = (b - a) / n
    x1 = np.arange(a+h, b, h)
    x2 = np.arange(a+h/2, b-h/2+h, h)
    I = h/6*(f(a)+f(b)+2*sum(f(x1))+4*sum(f(x2)))  
    
    # Dibujo
    
    plt.figure()
    # dibujo funcion a integrar en azul
    xx = np.linspace(a,b,endpoint=True)
    yy=f(xx)
    plt.plot(xx,yy,'b-',linewidth=3)
    # dibujo puntos de interpolacion en rojo 
    m = 2*n + 1
    nodos = np.linspace(a,b,num=m,endpoint=True)
    plt.plot(nodos,f(nodos),'ro')
    # dibujo poligonal en rojo
    xp = np.arange(a,b+h,h)
    for i in range(n):
        ptos = np.array([xp[i], x2[i], xp[i+1]])
        p = pol.polyfit(ptos,f(ptos),2)
        xxx = np.linspace(xp[i],xp[i+1])
        yy = p[0]+p[1]*xxx+p[2]*xxx**2
        plt.plot(xxx,yy,'r--',linewidth=2)
        plt.plot(np.array([xp[i], xp[i]]),np.array([0,f(xp[i])]),'r--',linewidth=2)
    
    plt.legend(['Área exacta', 'Puntos de interpolación',
            'Área aproximada'],loc='best') 
    plt.plot(np.array([a,a,b,b]),np.array([f(a),0,0,f(b)]),'b-',linewidth=2)        
    plt.plot(np.array([a,a]),np.array([0,f(a)]),'r--',linewidth=2)
    plt.plot(np.array([b,b]),np.array([0,f(b)]),'r--',linewidth=2)
    plt.plot(np.array([a,b]),np.array([0,0]),'r--',linewidth=2)
    plt.title('Fórmula de Simpson compuesta')
    plt.show()
    
    return I
#-----------------------

x = sym.Symbol('x', real=True) 
f = sym.log(x)
I_exacta = sym.integrate(f,(x,1,3))
I_exacta = float(I_exacta)

#-----------------------
f = lambda x : np.log(x)
a = 1.; b = 3; n = 4;
I = simpson_comp(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)
   