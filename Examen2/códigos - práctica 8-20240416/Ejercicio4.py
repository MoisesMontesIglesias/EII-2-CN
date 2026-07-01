# -*- coding: utf-8 -*-
"""
approximation with orthogonal basis
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import eval_legendre
np.set_printoptions(precision = 2)   # only 2 fractionary digits
np.set_printoptions(suppress = True) # do not use exponential notation

def approx3(f,deg,a,b):
    xp = np.linspace(a,b)
    yp = 0.
    
    for i in range(deg+1):
        g = lambda x: eval_legendre(i,(2*x-(a+b))/(b-a)) * f(x)
        num = quad(g,a,b)[0]
        g = lambda x: eval_legendre(i,(2*x-(a+b))/(b-a))**2
        den = quad(g,a,b)[0]
        p = num/den
        print('\na'+str(i)+' num = ',num)
        print('a'+str(i)+' den = ',den)
        print('a'+str(i)+'     = ',p)
        
        yp += p * eval_legendre(i,(2*xp-(a+b))/(b-a))
        
        
    plt.figure()
    plt.plot(xp,yp,label = 'polinomio de ajuste')
    plt.plot(xp,f(xp),'r',label='función')
    plt.legend()
    plt.show()       
    
# -------------------------------------------------
# first example
f1 = lambda x: np.sin(x)
a1 = 0.; b1 = 2.; deg1 = 2
approx3(f1,deg1,a1,b1)#,prin=True)    
# -------------------------------------------------
# second example
f2 = lambda x: np.cos(np.arctan(x)) - np.log(x+5)
a2 = -2.; b2 = 0.; deg2 = 4
approx3(f2,deg2,a2,b2)  