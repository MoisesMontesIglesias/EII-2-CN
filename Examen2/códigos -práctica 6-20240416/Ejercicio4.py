# -*- coding: utf-8 -*-
"""
Ejercicio 5
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
#%%----------------------------------------------------------------------------    
f = lambda x: np.cosh(x)*np.cos(x) - 1. 
a = 0.
b = 5.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x))
plt.plot([a,b],[0,0],'k-')
plt.plot(4.73,0,'ro')
plt.show()

#%%----------------------------------------------------------------------------
x0 = 4.5

raiz= op.newton(f,x0,tol=1.e-6,maxiter=100)       
        
print(raiz)


 