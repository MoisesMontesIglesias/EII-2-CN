# -*- coding: utf-8 -*-
"""
error_max()
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d, CubicSpline

def error_max():
    
    x= np.linspace(0,10,11)
    y=np.cos(x)
    
    xx=np.linspace(0,10,100)
    yy=np.cos(xx)
    
    f = interp1d(x, y, kind='linear')
    s = CubicSpline(x, y, bc_type='natural')
    
    plt.figure()
    plt.plot(x, y, 'o',label='nodos')
    plt.plot(xx, yy, '-',label='cos(x)')
    plt.plot(xx, f(xx), '-',label='P1')
    plt.plot(xx, s(xx), 'k-',label='spline')

    plt.legend(loc='best')
    plt.show()
    
    error1=np.linalg.norm(f(xx)-yy)    
    error2=np.linalg.norm(s(xx)-yy)
    
    print('Error interpolación lineal a trozos = %.5f'% error1)
    print('Error interpolación con splines     = %.5f'% error2)
#------------------------------------    
error_max()