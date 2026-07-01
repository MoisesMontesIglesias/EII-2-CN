#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Horner para un vector, vectorizado
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from Ejercicio2 import hornerV
#%%
def hornerVect(x,p):
    n = len(p)
    m = len(x)
    Y = np.zeros(m)
    Y = p[-1]
    for i in range(n-2,-1,-1):
        Y = Y*x+ p[i]
    return Y 
#%%
def main():
    p = np.array([1.,2,1])
    x = np.array([1.,-1])
    print('y = ',hornerVect(x,p))
    print('\n')

    #
    p = np.array([1., -1, 2, -3, 5, -2])
    x = np.linspace(-1,1)

    y = hornerVect(x,p)


    plt.figure()
    plt.plot(x,0*x,'k-')
    plt.plot(x,y)
    plt.title('P')


    #

    r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
    x = np.linspace(-1,1)

    y = hornerVect(x,r)

    plt.figure()
    plt.plot(x,0*x,'k-')
    plt.plot(x,y)
    plt.title('R')
    plt.show()


    #
    x = np.linspace(0,1,10**6)

    t = time.time()
    y = hornerV(x,p)
    tf = time.time()-t
    print('Tiempo sin vectorización = ', tf)

    t = time.time()
    y = hornerVect(x,p)
    tf = time.time()-t
    print('Tiempo con vectorización = ', tf)


if __name__ == "__main__":
    main()