# -*- coding: utf-8 -*-
"""
Ejercicio 1
"""
import numpy as np
import matplotlib.pyplot as plt

def lagrange_fundamental(i,x,z):
    n = len(x)

    ypf = 1.

    for k in range(n):
        if k != i :
            ypf *= (z-x[k]) / (x[i]-x[k]) 
    
    return ypf        
#%%----------------------------------------------------------------------------
def main():      
    x = np.array([-1., 0, 2, 3, 5])
    
    n = len(x)
    xp = np.linspace(min(x),max(x),100)
    
    y0 = np.eye(n)
    
    for i in range(n): 
        ypf = lagrange_fundamental(i,x,xp)
        
        plt.figure()
        plt.plot(xp,ypf)
        plt.plot(x,y0[i,],'o')
        plt.plot(xp,0*xp,'k-')
        plt.title('L'+str(i),fontsize=18)    
        #plt.show()

if __name__ == "__main__":
    main()
    