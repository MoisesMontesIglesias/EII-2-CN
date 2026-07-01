# -*- coding: utf-8 -*-
"""
Ejercicio 3
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy.polynomial.polynomial as pol
np.set_printoptions(suppress = True) # no usar notación exponencial
np.set_printoptions(precision = 2)   # solo dos decimales
#%%----------------------------------------
f1 = lambda x: np.sin(x)
a = 0; b= 2
g = 2 

def aprox2(f,g,a,b,pr=False):
                       
    A = np.zeros((g+1,g+1))    # matriz de coeficientes
    c = np.zeros(g+1)           # término independiente
    for i in range(g+1):
        for j in range(g+1):
            exponente = i+j
            integrando_A = lambda x : x**exponente
            # integrate.quad devuelve la integral y una cota del error
            # tomamos solo el primer elemento, el valor de la integral
            A[i,j]=quad(integrando_A,a,b)[0] 
        integrando_b = lambda x : (x ** i) * f(x)
        c[i]=quad(integrando_b,a,b)[0] 
    
    p = np.linalg.solve(A, c)
   
    
    if pr == True:    
        print('\n Matriz del sistema\n')
        print(A)
        print(u'\n\n Término independiente\n')
        print(c)
        
        
        print('\n\n Coeficientes del polinomio:\n')
        print(p)
    
    xx = np.linspace(a,b)
    yy = pol.polyval(xx,p)
    
    plt.figure()
    plt.plot(xx,f(xx),'r-',label='función exacta')  # dibujamos los puntos
    plt.plot(xx,yy,label='función aproximada')       # dibujamos el polinomio

    plt.legend()
    plt.show()

#%%---------------------------------------- 
f1 = lambda x: np.sin(x)
f2 = lambda x: np.cos(np.arctan(x)) - np.log(x+5) 
aprox2(f1,2,0.,2.,pr=True)
aprox2(f2,4,-2.,0.)

