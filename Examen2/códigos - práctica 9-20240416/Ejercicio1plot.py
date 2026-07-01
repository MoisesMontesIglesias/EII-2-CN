import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

def dibujo(f,a,b,nodos):
    plt.figure()
    ## Área exacta (function: blue 'b')
    # Top: function
    xp = np.linspace(a,b) # 50  points
    plt.plot(xp,f(xp),'b',label = 'Área exacta')
    # Closure
    plt.plot([a,a,b,b],[f(a),0,0,f(b)],'b')
    
    # Interpolation points (red points: 'ro')
    plt.plot(nodos,f(nodos),'ro',label = 'Puntos de interpolación')
    
    # Approximate area (red dashed line: 'r--')
    # interpolation polynomial
    p = pol.polyfit(nodos,f(nodos),len(nodos)-1)
    xp = np.linspace(a,b) # 50  points
    yp = pol.polyval(xp,p)
    plt.plot(xp,yp,'r--',label = 'Área aproximada')
    # closure
    pa = pol.polyval(a,p)
    pb = pol.polyval(b,p)
    plt.plot([a,a,b,b],[pa,0,0,pb],'r--')
    
    plt.legend()
    plt.show()    
    
f = lambda x: np.exp(x)
a = 0.; b = 3.; nodos = np.array([1,2,2.5])
dibujo(f,a,b,nodos) 

f = lambda x: np.cos(x) + 1.5
a = -3.; b = 3.; nodos = np.array([-3.,-1,0,1,3])
dibujo(f,a,b,nodos)   