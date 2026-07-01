import matplotlib.pyplot as plt
import numpy as np
##EJERCICIO6
def f(x):
    return x * np.e ** x

print(f(2))

def g(z):
    return z / (np.sin(z) * np.cos(z))

print(g(np.pi/4))

def h(x,y):
    return (x*y)/(x**2 + y**2)

print(h(2,4))

