# -*- coding: utf-8 -*-
"""
Ejercicio7
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


f = lambda x : x   # función
aa = 0.; bb = 3.   # intervalo
n = 5              # numero de iteraciones

T = bb - aa               # periodo

xx  = np.linspace(aa,bb,100)

# inicializamos la serie con el término constante
a0 = quad(f,aa,bb)[0]/T
s = a0

for k in range(n):
    # calculamos ak y bk
    fun1 = lambda x : np.cos(2.*np.pi*(k+1.)*x/T)*f(x)
    fun2 = lambda x : np.sin(2.*np.pi*(k+1.)*x/T)*f(x)
    
    ak=2.*quad(fun1,aa,bb)[0]/T
    bk=2.*quad(fun2,aa,bb)[0]/T
    
    # calculamos un término y lo sumamos a la serie
    s1 = ak * np.cos(2.*np.pi*(k+1.)*xx/T) + bk * np.sin(2.*np.pi*(k+1.)*xx/T) 
    s = s + s1
    
# dibujamos la función
plt.figure()
plt.plot(xx,f(xx),'b-',label='f')
    
# dibujamos los términos de la serie de Fourier
plt.plot(xx,s,'r',label='Serie')
plt.legend()
    
plt.title('f(x) = x en [0,3] para k = '+str(k+1)) 
plt.show()

    
 #%%----------------------------------------------------------
def Ejercicio5b():
    
    f = lambda x : (x - np.pi)**2   # función
    aa = 0.; bb = 2.*np.pi          # intervalo
    n = 6                           # numero de iteraciones

    T = bb - aa               # periodo

    xx = np.linspace(aa,bb)

    a0 = quad(f,aa,bb)[0]/T
    s = a0
    for k in range(n):
       # calculamos ak y bk
       fun1 = lambda x : np.cos(2.*np.pi*(k+1.)*x/T)*f(x)
       fun2 = lambda x : np.sin(2.*np.pi*(k+1.)*x/T)*f(x)
       ak=2.*quad(fun1,aa,bb)[0]/T
       bk=2.*quad(fun2,aa,bb)[0]/T
       # calculamos el término y lo sumamos a la serie
       s1 = ak * np.cos(2.*np.pi*(k+1.)*xx/T) + bk * np.sin(2.*np.pi*(k+1.)*xx/T);
       s = s + s1
    # dibujamos la función
    plt.figure()
    plt.plot(xx,f(xx),'b-',label='f')
    # dibujamos los términos de la serie de Fourier
    plt.plot(xx,s,'r',label='Serie')
    plt.legend()
    # dibujamos otros dos periodos de la función
    plt.title('f(x) = x en [0,2$\pi$] k = '+str(k+1))
    plt.show()
    
Ejercicio5b()  