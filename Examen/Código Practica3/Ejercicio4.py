#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ruffini
"""
import numpy as np
from Ejercicio1 import horner
#%%
def divisores(m):
    m = abs(int(m))
    div = np.zeros(2*m)
    cont = 0
    for i in range(1,m+1):
        if np.remainder(m,i) == 0:
            div[cont] = i
            div[cont+1] = -i
            cont += 2
    div = div[:cont]
    return div        
#%%   
def raices(p):
    n = len(p)
    m = p[0]
    div = divisores(m)
    
    r = np.zeros(n-1)
    cont = 0
    for i in range(len(div)):
        c, resto = horner(div[i],p)
        if resto == 0:
            r[cont] = div[i]
            cont += 1
    return r            
#%% 
def main():
    print('(a)\n')
    print('\nDivisores de 6')
    print(divisores(6))
    print('\nDivisores de 18')
    print(divisores(18))
    print('\nDivisores de 20')
    print(divisores(20))    

    print('\n\n(b)\n')
    #(x-1)(x+1)
    p0 = np.array([-1.,0,1])
    print('\nRaíces de p0\n')
    print(raices(p0))

    #(x-1)(x+2)(x-4)
    p1 = np.array([8., -6, -3, 1])
    print('\nRaíces de p1\n')
    print(raices(p1))
    #%%
    #(x-1)(x+1)(x-3)(x+5)
    p2 = np.array([15., -2, -16, 2, 1])
    print('\nRaíces de p2\n')
    print(raices(p2))
    #%%
    #(x-4)(x+1)(x+3)(x-5) 
    p3 = np.array([60.,53, -13, -5, 1])   
    print('\nRaíces de p3\n')
    print(raices(p3))
    #%%
    # (x+1)(x-2)(x+5)(x-7)(x+7)
    p4 = np.array([490., 343, -206, -56, 4, 1])     
    print('\nRaíces de p4\n')
    print(raices(p4))
    #%%
if __name__ == "__main__":
    main() 
