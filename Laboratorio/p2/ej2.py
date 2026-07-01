import numpy as np
import matplotlib.pyplot as plt
#Ejercicio2

def f(x):
    return np.e**x

def funExp(x, tol, maxNumSum):
    sumando = 0
    i = 0
    factorial = 1
    termino = 0
    error = np.inf
    while (error > tol and i < maxNumSum):
        termino = x ** i / factorial
        sumando += termino
        error = np.max(termino)
        i += 1
        factorial *= i
    
    return sumando
x = np.linspace(-1,1,50)
tol = 1.e-8
maxNumSum = 100
y = funExp(x,tol,maxNumSum)
plt.figure()
plt.plot(x,f(x),'y',linewidth = 4)
plt.plot(x,y,'b--')
plt.plot(x,x*0,'k')
plt.title("Ejercicio 2")
plt.legend()
plt.show()


