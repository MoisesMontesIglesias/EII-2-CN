# -*- coding: utf-8 -*-
"""
Ejercicio 3
"""
import numpy as np
import matplotlib.pyplot as plt
from Ejercicio1 import lagrange_fundamental
#%%----------------------------------------------------------------------------
def polinomio_lagrange(x,y,xp):
    n = len(x)
    yp = 0.
    for i in range(n):
        yp += y[i] * lagrange_fundamental(i,x,xp)
    return yp
#%%----------------------------------------------------------------------------

x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])


xp = np.linspace(min(x),max(x),100)
yp = polinomio_lagrange(x,y,xp)

plt.figure()
plt.plot(x,y,'ro',label='puntos')
plt.plot(xp,yp,label='P')
plt.legend()
plt.show()   
#%%----------------------------------------------------------------------------
x = np.array([-1., 0, 2, 3, 5, 6, 7])
y = np.array([ 1., 3, 4, 3, 2, 2, 1])

xp = np.linspace(min(x),max(x),100)
yp = polinomio_lagrange(x,y,xp)

plt.figure()
plt.plot(x,y,'ro',label='puntos')
plt.plot(xp,yp,label='P')
plt.legend()
#plt.show() 

    