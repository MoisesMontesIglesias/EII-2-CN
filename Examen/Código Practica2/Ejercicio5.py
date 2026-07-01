#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taylor
"""
import numpy as np         
     

x = 0.5

fact1 = 1
fact2 = 1

co = 0.
si = 0.
tant = np.inf

error = 1.
k = 0

while error > 1.e-4:

    co += x**(2*k)/fact1
    si += x**(2*k+1)/fact2
    t = si/co
    
    error = abs(t-tant)

    tant = t
    
    k += 1
    fact1 *= 2*k * (2*k-1)
    fact2 *= (2*k+1) * 2*k
    
print('Valor aprox  = ', t)
print('Valor exacto = ', np.tanh(x)) 
