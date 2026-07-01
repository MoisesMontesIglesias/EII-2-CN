# -*- coding: utf-8 -*-
"""
aproximación con función logística
"""
import numpy as np
import numpy.polynomial.polynomial as pol 
import matplotlib.pyplot as plt
import pandas as pd

def reg(t,P,L):
    x = np.copy(t)
    y = np.log((L-P)/P)
    
    A = np.zeros((2,2))
    b = np.zeros(2)
    
    A[0,0] = len(t)
    A[0,1] = np.sum(x)
    A[1,0] = A[0,1]
    A[1,1] = np.sum(x**2)
    
    b[0] = np.sum(y)
    b[1] = np.sum(x*y)
    
    a = np.linalg.solve(A,b)
    
    c = np.exp(a[0])
    K = a[1]

    
    f = lambda x: L / (1+c*np.exp(K*x))
    xp = np.linspace(min(x),max(x))
    
    plt.figure()
    plt.plot(x,y,'bo',label='puntos')
    plt.plot(xp,a[0]+a[1]*xp,'r',label='función aproximada')
    plt.xlabel('t')
    plt.ylabel('log((L-P)/P)')
    plt.legend()
    plt.show()
    
    plt.figure()
    plt.plot(t,P,'bo',label='puntos')
    plt.plot(xp,f(xp),'r',label='función aproximada')
    plt.xlabel('t')
    plt.ylabel('P')
    plt.legend()
    plt.show()
    
    return c, K
# primer ejemplo
print('---------------------  EJEMPLO TELEFONIA  ---------------------')
datos = pd.read_csv('Telefonia.csv')
t = datos['Fecha']
t = t - t[0]
P = datos['Porcentaje']
L = 100
    
c, K = reg(t,P,L)
print('c = ',c,' K = ',K) 

# segundo ejemplos
print('\n\n---------------------  EJEMPLO FOCAS  ---------------------')
datos = pd.read_csv('Focas.csv')
t = datos['Fecha']
t = t - t[0]
P = datos['Focas']
L = 25500

c, K = reg(t,P,L)
print('c = ',c,' K = ',K) 
    
