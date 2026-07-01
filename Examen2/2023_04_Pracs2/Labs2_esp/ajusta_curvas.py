#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajusta curvas por minimos cuadrados
"""
"""
EJERCICIO 2
"""
import numpy as np
import matplotlib.pyplot as plt
#%%----------------------------------------------
def g1(x,p):    
    return  p[0]* np.exp(-p[1] * x) + p[2]
#%%
def g2(x,p):    
    return  p[2]* (1-p[0]*np.exp(p[1] * x))
#%%
def g3(x,p):
    return p[0] * np.exp(-p[1]*x**2) + p[2]
#%%
def genera_datos(k):
    if k == 1:
        np.random.seed(10)
        t = np.linspace(0.3, 3, 100)
        Q = g1(t, [2.5, 1.3, 0.5])
        np.random.seed(1)
        Q_noise = 0.1 * np.random.normal(size=t.size) 
        Q += Q_noise                   
        bounds = np.array([3.,2,1])
    if k == 2:
        np.random.seed(20)
        t = np.linspace(-3, 3.1, 100)
        Q = g2(t, [2.9, 0.5, 0.8])
        Q_noise = 0.5 * np.random.normal(size=t.size) 
        Q +=  Q_noise
        bounds = np.array([3.,1,1])
    if k == 3:    
        np.random.seed(30)
        t = np.linspace(-2,2, 100)
        Q = g3(t, [0.8, 1.8, 0.1])
        Q_noise = 0.03 * np.random.normal(size=t.size) 
        Q += Q_noise
        bounds = np.array([1.,2,1])
    return t,Q, bounds    
#%%----------------------------------------------
def residual(t,Q,g,p):
    return np.sum((g(t,p) - Q)**2)
#%%----------------------------------------------
def ajusta_curva(t,Q,g,bordes):
    mejor_residual = np.inf
    for k in range(200):
        
        p = np.random.rand(len(bordes))*bordes
        r = residual(t,Q,g,p)
        
        if r < mejor_residual:
            mejor_residual = r
            mejores_parametros = np.copy(p)
            
    return mejores_parametros, mejor_residual        
#%%------------------------------------------------------        
def plot(t,Q,g,p): 
    plt.figure()
    plt.plot(t,Q,'bo')
    plt.plot(t,g(t,p),'r')
    plt.show()
#%%------------------------------------------------------
t1, Q1, bordes1 =  genera_datos(1)
t2, Q2, bordes2 =  genera_datos(2)
t3, Q3, bordes3 =  genera_datos(3)
#%%
print('\n--------------- Ejercicio 2.1. ---------------')
print('residual 1 = ', residual(t1,Q1,g1,[1.,1.,1.]))
print('residual 2 = ', residual(t2,Q2,g2,[0.2,0.2,0.2]))
print('residual 3 = ', residual(t3,Q3,g3,[3.,3.,3.]))
#%%

print('\n--------------- Ejercicio 2.2. ---------------')
print('          Parámetros óptimos  Residuales')
p_opt1, r1 = ajusta_curva(t1,Q1,g1,bordes1)
print('Ajuste 1 ',p_opt1,'  ', r1)
p_opt2, r2 = ajusta_curva(t2,Q2,g2,bordes2)
print('Ajuste 2 ',p_opt2,'  ', r2) 
p_opt3, r3 = ajusta_curva(t3,Q3,g3,bordes3)
print('Ajuste 3 ',p_opt3,'  ', r3) 
#%%

print('\n--------------- Ejercicio 2.3. ---------------')
plot(t1,Q1,g1,p_opt1)
plot(t2,Q2,g2,p_opt2)
plot(t3,Q3,g3,p_opt3)
