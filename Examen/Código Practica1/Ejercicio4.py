#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Añade ceros al principio y al final
"""
import numpy as np
a = np.array([1.,2,3])

#%%
b = np.append(a,0)
b = b[::-1]
b = np.append(b,0)
b = b[::-1]
print('\n1.')
print('b = ',b)
#%%
b = np.zeros(5)
b[1:4] = a
print('\n2.')
print('b = ',b)

#%%
c = np.zeros(1)
b = np.concatenate((c,a,c))
print('\n3.')
print('b = ',b)

