# -*- coding: utf-8 -*-
"""
Ejercicio 2
"""
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

def diferencias_divididas(nodos,valores):
    n = len(nodos)
    
    tabla = np.zeros((n,n+1))
    
    tabla[:,0] = nodos
    tabla[:,1] = valores
    
    for j in range(2,n+1):
        for i in range(n-j+1):
            num = tabla[i+1,j-1] - tabla[i,j-1]
            den = tabla[i+j-1,0] - tabla[i,0]
            tabla[i,j] = num/den    
    
    return tabla
#%%----------------------------------------------------------------------------
nodos   = np.array([-1., 0, 2, 3, 5])
valores = np.array([ 1., 3, 4, 3, 1])

tabla = diferencias_divididas(nodos,valores)
print('TABLA DE DIFERENCIAS DIVIDIDAS')
print(tabla)
#%%----------------------------------------------------------------------------
def polinomio_newton(xx,nodos,valores):
    a = diferencias_divididas(nodos,valores) 

    n = len(nodos)
    
    produ = 1.
    yy = 0.
    
    for i in range(n):
        yy += a[0,i+1] * produ
        produ *= (xx-nodos[i])
        
    return yy    
#%%----------------------------------------------------------------------------
nodos   = np.array([-1., 0, 2, 3, 5])
valores = np.array([ 1., 3, 4, 3, 1])

xx = np.linspace(min(nodos),max(nodos),100)

yy = polinomio_newton(xx,nodos,valores)

plt.figure()
plt.plot(xx,yy)
plt.plot(nodos,valores,'ro')
plt.show()
#%%----------------------------------------------------------------------------
nodos   = np.array([-1., 0, 2, 3, 5, 6, 7])
valores = np.array([ 1., 3, 4, 3, 2, 2, 1])

xx = np.linspace(min(nodos),max(nodos),100)

yy = polinomio_newton(xx,nodos,valores)

plt.figure()
plt.plot(xx,yy)
plt.plot(nodos,valores,'ro')
plt.show()
       