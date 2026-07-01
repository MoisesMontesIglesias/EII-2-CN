# -*- coding: utf-8 -*-
"""
Ejercicio 1
"""
#---------------------- Import modules
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
#---------------------- Function 1
def Vandermonde(x):
    n = len(x)  
    V = np.ones((n,n))
    for i in range(1,n):
        V[:,i] = V[:,i-1]*x
    return V     
#---------------------- Function 2
def polVandermode(x,y):
    V = Vandermonde(x)
    p = np.linalg.solve(V,y)
    return p
#----------------------- Data 
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

x1 = np.array([-1., 0, 2, 3, 5, 6, 7])
y1 = np.array([ 1., 3, 4, 3, 2, 2, 1])

#------------ Call the function
p = polVandermode(x,y)
p1 = polVandermode(x1,y1)

#----------------------  Plot 1
xp = np.linspace(min(x),max(x))
yp = pol.polyval(xp,p)

plt.figure()
plt.plot(x,y,'ro',label = 'nodos')
plt.plot(xp,yp,label = 'P')
plt.legend()
plt.show()

#----------------------  Plot 2
xp1 = np.linspace(min(x1),max(x1))
yp1 = pol.polyval(xp1,p1)

plt.figure()
plt.plot(x1,y1,'ro',label = 'nodos')
plt.plot(xp1,yp1,label = 'P')
plt.legend()
#plt.show()

#----------------------  Partial results
V = Vandermonde(x)
p = np.linalg.solve(V,y)

