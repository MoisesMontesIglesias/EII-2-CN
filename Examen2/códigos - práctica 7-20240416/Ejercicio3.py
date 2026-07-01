## module cheby
# -*- coding: utf-8 -*-
"""
cheby(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol


def chebyshev(f,a,b,n):
    
    index1 = np.array(range(n)).astype('float')
    xe = a+((b-a)/(float(n)-1.))*index1
    xe = np.linspace(a,b,n)
    
    index2 = np.arange(1,n+1)
    xc=np.cos(((2.*index2-1)*np.pi)/(2.*float(n)))
    
    xx=np.linspace(a,b,500)
 
    pe=pol.polyfit(xe,f(xe),n-1)
    pc=pol.polyfit(xc,f(xc),n-1)  
    
    plt.figure()   
    plt.plot(xx,f(xx),'b',label=u'función')
    plt.plot(xe,f(xe),'ro',label='nodos')
    plt.plot(xx,pol.polyval(xx,pe),'r',label='polinomio')
    plt.title('Nodos equiespaciados')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc='best')
    plt.show()
    
    plt.figure() 
    plt.plot(xx,f(xx),'b',label=u'función')
    plt.plot(xc,f(xc),'ro',label='nodos')
    plt.plot(xx,pol.polyval(xx,pc),'r',label='polinomio')
    plt.title('Nodos Chebyshev')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc='upper center')
    plt.show()
#-------------------------------------------------------
f = lambda x : 1/(1+25*x**2) # definimos la función
a = -1.; b =  1.; n = 11  
print('------------  Función f1  ------------')
chebyshev(f,a,b,n)  
#-------------------------------------------------------
f = lambda x : np.exp(-20*x**2) # definimos la función
a = -1.; b =  1.; n = 15   
print('\n\n------------  Función f2  ------------')
chebyshev(f,a,b,n)   
       
