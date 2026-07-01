import numpy as np
import matplotlib.pyplot as plt
#Ejercicio3
def f(x):
    return np.sin(x)

x0 = np.pi/4
tol = 1.e-8
maxNumSum = 100
i = 0
suma = 0
factorial = 1
contador = 0
error = np.inf
while i < maxNumSum and error > tol:
    termino = x0 ** i / factorial
    if (contador//2 == 0):
        suma += termino
    else:
        suma-=termino
    
    error = np.abs(termino)
    i += 2
    factorial *= i
    contador+=1


print("Valor aprox: ", suma)
print("Valor exacto: ", f(x0))
print("Número de iteraciones: ", i) 