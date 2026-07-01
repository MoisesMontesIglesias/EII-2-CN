# -*- coding: utf-8 -*-
"""
Ejercicio 7
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
#%%----------------------------------------------------------------------------    
f = lambda x: x**3 - 75. 
a = 0.
b = 5.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x))
plt.plot([a,b],[0,0],'k-')
plt.plot(4.2172,0,'ro')
plt.show()

#%%----------------------------------------------------------------------------
x0 = 4.5

raiz, r = op.bisect(f,4,5,full_output=True)       
        
print(raiz)
