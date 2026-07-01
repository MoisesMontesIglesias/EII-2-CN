import matplotlib.pyplot as plt
import numpy as np
##EJERCICIO7
x = np.linspace(-2* np.pi,2*np.pi,200)              # malla
f = lambda x : x * np.sin(3*x)   # función 
OX = 0*x
plt.figure()
plt.plot(x,f(x))                   # dibujar la función
plt.plot(x,OX,'k-')                # dibujar el eje X
plt.xlabel('x')
plt.ylabel('y')
plt.title('función')
plt.show()






