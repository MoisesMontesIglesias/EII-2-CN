# -*- coding: utf-8 -*-
"""
Ejercicio 1
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

np.set_printoptions(suppress = True) # no usar notación exponencial
np.set_printoptions(precision = 2)   # solo dos decimales
#%%----------------------------------------
def Vandermonde(x,k):
      
    k = k+1
    n = len(x)
    V = np.zeros((n,k))
    for i in range(n):
        for j in range(k):
            V[i,j] = x[i]**j
    
    return V
#%%---------------------------------------- 
def aprox1(f,g,a,b,n,pr=False):

    x = np.linspace(a,b,n)
    y = f(x)   
    
    # Calculamos la matriz de Vandermonde
    V = Vandermonde(x,g)
    
    A = np.dot(V.transpose(),V)
    c = np.dot(V.transpose(),y)
    p = np.linalg.solve(A, c)
    
    if pr == True:
        print('\n Matriz del sistema\n')
        print(A)
        print(u'\n\n Término independiente\n')
        print(c)
        print(u'\n\n Solución del sistema\n')
        print(p)



    xx = np.linspace(min(x),max(x))
    yy = pol.polyval(xx,p)

    plt.figure()
    plt.plot(x,y,'ro',label='puntos')            # dibujamos los puntos
    plt.plot(xx,yy,label='función aproximada')               # dibujamos el polinomio
    plt.legend(); 
    plt.show()   

#%%---------------------------------------- 
f1 = lambda x: np.sin(x)
f2 = lambda x: np.cos(np.arctan(x)) - np.log(x+5) 
aprox1(f1,2,0.,2.,5,pr=True)
aprox1(f2,4,-2.,0.,10,pr=True)


