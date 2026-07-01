# -*- coding: utf-8 -*-
"""
Ejercicio 6
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import sympy as sym
#--------------------------------------------------------------------------
x = sym.Symbol('x', real=True)

f_sim = sym.exp(-x**2) * sym.log(x**2+1)
df_sim = sym.diff(f_sim,x)
d2f_sim = sym.diff(df_sim,x)

f  = sym.lambdify([x], f_sim,'numpy') 
df = sym.lambdify([x], df_sim,'numpy')
d2f = sym.lambdify([x], d2f_sim,'numpy')
#--------------------------------------------------------------------------
'''
a = -4.
b = 4.
x = np.linspace(a,b,1000)
plt.plot(x,df(x))
plt.plot([a,b],[0,0],'k-')
plt.title('Función derivada de f')
plt.show()
'''
#--------------------------------------------------------------------------
x0 = np.array([-1.,0.,1.])
x1 = np.zeros_like(x0)
for i in range(len(x0)):
    x1 [i] = op.newton(df,x0[i],tol=1.e-6,maxiter=100)  
#--------------------------------------------------------------------------
a = -3.
b = 3.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label = 'Función f')
plt.plot([a,b],[0,0],'k-')
plt.plot([x1[0],x1[2]],[f(x1[0]),f(x1[2])],'ro',label='Max')
plt.plot([x1[1]],[f(x1[1])],'go',label='min')
plt.legend(loc='best')
plt.show()
print('Extremos \n', x1)
#%%--------------------------------------------------------------------------
'''
a = -3.
b = 3.
x = np.linspace(a,b,1000)
plt.plot(x,d2f(x))
plt.plot([a,b],[0,0],'k-')
plt.title('Función derivada segunda de f')
plt.show()
'''
#--------------------------------------------------------------------------
x0 = np.array([-1.5,-0.5,0.5,1.5])
x1 = op.newton(d2f,x0,tol=1.e-6,maxiter=100)  

#--------------------------------------------------------------------------
a = -3.
b = 3.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label = 'Función f')
plt.plot([a,b],[0,0],'k-')
plt.plot(x1,f(x1),'bo',label='Puntos de Inflexión')
plt.legend(loc='best')
plt.show()
print('\nPuntos de inflexión \n', x1)
#%%--------------------------------------------------------------------------

