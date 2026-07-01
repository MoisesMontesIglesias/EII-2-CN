#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajusta una curva por minimos cuadrados
"""
import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)
#%%----------------------------------------------
def genera_datos1():
    g = lambda x,p: p[2]* (1-p[0]*np.exp(p[1] * x))
    np.random.seed(20)
    t = np.linspace(-3, 2.1, 100)
    Q = g(t, [1., 0.5, 0.8])
    Q_noise = 0.1 * np.random.normal(size=t.size) 
    Q +=  Q_noise
    return Q, t, g
#%%---------------------------------------------- 

Q, t, g = genera_datos1()


print('\n--------------- Ejercicio 1.1. ---------------')
x = np.copy(t)
y = np.log(1-Q/0.8)

print('x[10:20] = ',x[10:20])
print('y[10:20] = ',y[10:20])

print('\n--------------- Ejercicio 1.2. ---------------')
a0, a1 = pol.polyfit(x,y,1)
p = np.array([np.exp(a0),a1,0.8])
print('p = ', p)

print('\n--------------- Ejercicio 1.3. ---------------')
xp = np.linspace(min(t),max(t))
yp = g(xp,p)    

plt.figure()
plt.plot(t,Q,'bo',label='datos')
plt.plot(xp,yp,'r',label='Curva de ajuste')
plt.legend()
plt.show()      
    
