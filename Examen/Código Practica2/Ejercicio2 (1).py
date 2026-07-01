#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MacLaurin e^x
"""
import numpy as np
import matplotlib.pyplot as plt
#%% Dibujar la función exp(x) usando su polinomio de Taylor
def funExp(x0,tol,maxNumSum):

    suma = 0.
    error = np.inf
    iteraciones = 0
    factorial = 1.

    while (error > tol and iteraciones < maxNumSum):
        termino = x0**iteraciones/factorial
        suma += termino
        error = np.max(termino)

        iteraciones += 1
        factorial *= iteraciones

    return suma
#%% Con vectorizacion
f = lambda x: np.exp(x)
tol = 1.e-8
x = np.linspace(-1,1)
y = funExp(x, tol, 100)

plt.figure()
plt.plot(x,f(x),'y', linewidth = 4,label = 'f')
plt.plot(x,y,'b--',label = 'Aproximación f')
plt.plot(x,x*0,'k')
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()

def determinant_3x3(matrix, row):
    # Selecciona la fila para desarrollar el determinante
    submatrix = np.delete(matrix, row, axis=0)
    det = (
        matrix[row][0] * (submatrix[0][1]*submatrix[1][2] - submatrix[1][1]*submatrix[0][2]) -
        matrix[row][1] * (submatrix[0][0]*submatrix[1][2] - submatrix[1][0]*submatrix[0][2]) +
        matrix[row][2] * (submatrix[0][0]*submatrix[1][1] - submatrix[1][0]*submatrix[0][1])
    )
    return det

for j in range(n):
            sign = (-1) ** j
            submatrix = [row[:j] + row[j+1:] for row in (matrix[1:])]
            det += sign * matrix[0][j] * determinant(submatrix)
        return det