#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Horner para un vector, sin vectorizar
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
def hornerV(x,p):

    n = len(p)
    q = np.zeros(n)
    
    m = len(x)
    y = np.zeros_like(x)
    
    for k in range(m):
        x0 = x[k]
        q[-1] = p[-1]
    
        for i in range(n-2,-1,-1):
            q[i] = q[i+1]*x0 + p[i]
    

        y[k]  = q[0]    
    return y   
#%%
def main():
    p = np.array([1, -1, 2, -3,  5, -2])
    
    x = np.linspace(-1,1)
    
    y = hornerV(x,p)
    plt.plot(x,y)
    # plt.plot(x,pol.polyval(x,p))
    plt.plot(x,0*x,'k')
    plt.title('P')
    plt.show()
    
    #
    r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
    
    x = np.linspace(-1,1)
    
    y = hornerV(x,r)
    plt.plot(x,y)
    # plt.plot(x,pol.polyval(x,r))
    plt.plot(x,0*x,'k')
    plt.title('R')
    plt.show()

if __name__ == "__main__":
    main() 