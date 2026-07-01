import numpy as np
import matplotlib.pyplot as plt
#Ejercicio1
def f(x):
    return np.e**x

x0 = -0.4
tol = 1.e-8
maxNumSum = 100
i = 0
suma = 0
factorial = 1
error = np.inf
while i < maxNumSum and error > tol:
    termino = x0 ** i / factorial
    suma += termino
    error = np.abs(termino)
    i += 1
    factorial *= i


print("Valor de la función en -0.4: ", f(x0))
print("Valor de la aproximación en -0.4: ", suma)
print("Número de iteraciones: ", i)