## module trapecio_comp
# -*- coding: utf-8 -*-
"""
I = trapecio_comp(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def trapecio_comp(f,a,b,n):
       
    h = (b - a) / n
    x = np.arange(a+h, b, h)
    I = h*(f(a)+f(b))/2+h*np.sum(f(x));  
    
    # Dibujo
    
    plt.figure()
    # dibujo funcion a integrar en azul
    xx = np.linspace(a,b,endpoint=True)
    yy=f(xx)
    plt.plot(xx,yy,'b-',linewidth=2)
    # dibujo puntos de interpolacion en rojo 
    nodos = np.concatenate([np.array([a]),x,np.array([b])])
    plt.plot(nodos,f(nodos),'ro')
    # dibujo poligonal en rojo
    plt.plot(nodos,f(nodos),'r--',linewidth=2)
    plt.legend(['Área exacta', 'Puntos de interpolación',
           'Área aproximada'],loc='best')    
    # dibujo contorno areas
    plt.plot(np.array([a,a,b,b]),np.array([f(a),0,0,f(b)]),'b-',linewidth=2)    
    
    
    for i in range(n-1):
        plt.plot(np.array([x[i],x[i]]),[0,f(x[i])],'r--',linewidth=2)


    plt.plot(np.array([a,a]),np.array([0,f(a)]),'r--',linewidth=2)
    plt.plot(np.array([b,b]),np.array([0,f(b)]),'r--',linewidth=2)
    plt.plot(np.array([a,b]),np.array([0,0]),'r--',linewidth=2)
    plt.title('Fórmula del Trapecio compuesta')
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
I = trapecio_comp(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)