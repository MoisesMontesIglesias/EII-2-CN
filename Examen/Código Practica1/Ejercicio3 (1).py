#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slicing
"""
import numpy as np

v = np.arange(0,13,1.1)
print('v = ', v)

print('\nvi = ', v[::-1])

print('\nv1 = ', v[0::2])
print('v2 = ', v[1::2])

print('\nv1 = ', v[0::3])
print('v2 = ', v[1::3])
print('v3 = ', v[2::3])

print('\nv1 = ', v[0::4])
print('v2 = ', v[1::4])
print('v3 = ', v[2::4])
print('v4 = ', v[3::4])
