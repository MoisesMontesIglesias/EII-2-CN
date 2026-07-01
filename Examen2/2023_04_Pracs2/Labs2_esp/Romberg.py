#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Romberg
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
np.set_printoptions(precision = 6)   
np.set_printoptions(suppress = True) 

def puntos_medios(x):
    n = len(x)
    pm = np.zeros(n-1)
    todos = np.zeros(2*n-1)
    k = 0
    for i in range(n-1):        
        pm[i] = (x[i+1] + x[i]) / 2
        todos[k] = x[i]
        todos[k+1] = pm[i]
        k += 2
    todos[-1] = x[-1]    
    return pm, todos
#%%
def dibuja(f,a,b,nodos):
    x = np.linspace(a,b)
    plt.figure(figsize=(4,3))
    plt.plot(x,f(x),'b')
    plt.plot(nodos,f(nodos),'r--',[a,b],[0,0],'r--')
    for i in range(len(nodos)):
        plt.plot([nodos[i],nodos[i]],[0,f(nodos[i])],'r--')
    plt.show()
#%%
def columna_cero(f,a,b,n):
    I0 = np.zeros(n)
    h = b-a
    I0[0] = h/2*(f(a)+f(b))
    todos = np.array([a,b])
    for i in range(1,n):
        h /= 2.
        pm, todos = puntos_medios(todos)
        I0[i] = I0[i-1]/2 + h * np.sum(f(pm))    
    return I0    
#%%
def Romberg(f,a,b,n):
    I = np.zeros((n,n))
    I[:,0] = columna_cero(f,a,b,n)
    for j in range(1,n):
        for i in range(j,n):
            I[i,j] = (4**j * I[i,j-1] - I[i-1,j-1]) /(4**j-1) 
    return I
#%%
def Romberg2(f,a,b):
    h = b-a
    Ip = np.array([(b-a)/2*(f(a)+f(b))])
    todos = np.array([a,b])
    print(Ip)
    error = np.inf
    i = 1
    while error > 1.e-07:
        h /= 2.
        pm, todos = puntos_medios(todos)
        I = np.zeros(i+1)
        I[0] = Ip[0]/2 + h * np.sum(f(pm)) 
        
        for j in range(1,i+1):
            I[j] = (4**j * I[j-1] - Ip[j-1]) /(4**j-1) 
            
        print(I) 
        error = np.abs(I[-1]-Ip[-1])
        Ip = np.copy(I)
        i += 1    
    return I[-1]    
#%%
print('==============  EJERCICIO 1  ==============')
x = np.linspace(0,5,6)
pm, todos = puntos_medios(x)

print('x')
print(x)
print('puntos medios')
print(pm)
print('todos')
print(todos)    

      
x = np.copy(todos)
pm, todos = puntos_medios(x)
print('\nx')
print(x)
print('puntos medios')
print(pm)
print('todos')
print(todos)   
print('\n==============  EJERCICIO 2  ==============\n')
f1 = lambda x: np.sin(x)
a1 = 0.; b1 = 2.; n1 = 2
nodos1 = np.linspace(a1,b1,2**n1+1)
dibuja(f1,a1,b1,nodos1)

f2 = lambda x: x**2 + np.log(2*x+7) * np.cos(3*x) + 1.5
a2 = -2.; b2 = 4.; n2 = 3
nodos2 = np.linspace(a2,b2,2**n2+1)
dibuja(f2,a2,b2,nodos2)

print('\n==============  EJERCICIO 3  ==============\n')
print('Primer ejemplo columna cero')
I1 = columna_cero(f1,a1,b1,4)
print(I1)

print('\nSegundo ejemplo columna cero')
I2 = columna_cero(f2,a2,b2,5)
print(I2)
#%%
print('\n==============  EJERCICIO 4  ==============\n')
t = sym.Symbol('t', real=True) 

print('---- Primer ejemplo Romberg ----\n')
n = 4
I= Romberg(f1,a1,b1,n)

f_sim = sym.sin(t)
I_exacta = sym.integrate(f_sim,(t,0,2))
Ie1 = float(I_exacta)

print('Matriz')
print(I)
print('\nValor con',2**(n-1),'intervalos         ', I[n-1,0])
print('Valor con corrección del error ', I[n-1,n-1])
print('Valor exacto                   ', Ie1)

print('\n---- Segundo ejemplo Romberg ----\n')
n = 6       
I= Romberg(f2,a2,b2,n)

f_sim = t**2 + sym.log(2*t+7) * sym.cos(3*t) + 1.5
I_exacta = sym.integrate(f_sim,(t,-2,4))
Ie2 = float(I_exacta)

print('Matriz')
print(I)
print('\nValor con',2**(n-1),'intervalos        ', I[n-1,0])
print('Valor con corrección del error ', I[n-1,n-1])
print('Valor exacto                   ', Ie2)
#%%
'''
print('\n==============  EJERCICIO 5  ==============\n')


print('---- Primer ejemplo Romberg ----\n')
sol = Romberg2(f1,a1,b1)
print('El resultado final es ',sol)

print('\n---- Segundo ejemplo Romberg ----\n')     
sol = Romberg2(f2,a2,b2)
print('El resultado final es ',sol)

#%%

from scipy import integrate
uno = integrate.romberg(f1, a1, b1, show = True)
  
print(uno)

dos = integrate.romberg(f2, a2, b2, show = True)
 
print(dos)
'''
