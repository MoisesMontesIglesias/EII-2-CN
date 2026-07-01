## module punto_medio_comp
# -*- coding: utf-8 -*-
"""
I = punto_medio_comp(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


def punto_medio_comp(f,a,b,n):
    
    h = (b - a) / n
    x = np.arange(a+h/2, b, h)
    I = np.sum(f(x))*h;  
    
    # Dibujo
    
    plt.figure()
    # dibujo funcion a integrar en azul
    xx = np.linspace(a,b,endpoint=True)
    yy=f(xx)
    plt.plot(xx,yy,'b-',linewidth=2)
    # dibujo puntos de interpolacion en rojo 
    plt.plot(x,f(x),'ro')
    # dibujo poligonal en rojo
    for i in range(n):
        aa = np.array([x[i]-h/2, x[i]+h/2])
        bb = np.array([f(x[i]), f(x[i])])
        plt.plot(aa,bb,'r--',linewidth=2)

        plt.legend(['Área exacta', 'Puntos de interpolación',
                    'Área aproximada'],loc='best')
        # dibujo contorno areas
        plt.plot(np.array([a,a,b,b]),np.array([f(a),0,0,f(b)]),
                'b-',linewidth=2)
    for i in range(n):
        plt.plot(np.array([x[i]-h/2, x[i]-h/2]),np.array([0,f(x[i])]),
                'r--',linewidth=2)

    plt.plot(np.array([x[i]+h/2, x[i]+h/2]),np.array([0, f(x[i])]),
            'r--',linewidth=2)
    plt.plot(np.array([a,b]),np.array([0.,0.]),'r--',linewidth=2)
    plt.title('Fórmula del Punto Medio compuesta')
    plt.show()
    
    return I
#-----------------------

x = sym.Symbol('x', real=True) 
f = sym.log(x)
I_exacta = sym.integrate(f,(x,1,3))
I_exacta = float(I_exacta)

#-----------------------
f = lambda x : np.log(x)
a = 1.; b = 3; n = 5;
I = punto_medio_comp(f,a,b,n)
print ('El valor aproximado es', I )
print ('El valor exacto es    ', I_exacta)