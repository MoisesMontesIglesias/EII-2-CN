#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos student
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy.polynomial.polynomial as pol
#%%------------------------------

#http://archive.ics.uci.edu/ml/datasets/Auto+MPG
#0. mpg: continuous
#1. cylinders: multi-valued discrete
#2. displacement: continuous
#3. horsepower: continuous
#4. weight: continuous
#5. acceleration: continuous
#6. model year: multi-valued discrete
data = pd.read_csv('http://www.unioviedo.es/compnum/laboratorios_py/new/cars.csv',sep=',')
#data = pd.read_csv('cars.csv',sep=',')
#%%

x = data['weight']
y = data['horsepower']



p = pol.polyfit(x,y,1)
xx = np.linspace(min(x),max(x))
yy = pol.polyval(xx,p)

punto = 3000
valor = pol.polyval(punto,p)

print(int(valor), 'caballos')

plt.figure()
plt.plot(x,y,'o')
plt.plot(xx,yy,'r-')
plt.xlabel('weight')
plt.ylabel('horsepower')
plt.plot(punto,pol.polyval(punto,p),'ro')
plt.plot([punto,punto,1300],[20,pol.polyval(punto,p),pol.polyval(punto,p)],'r--')
plt.axis([1500,5300,30,250])
plt.show()

#%%
x = data['horsepower']
y = data['mpg']


p = pol.polyfit(x,y,2)
xx = np.linspace(min(x),max(x))
yy = pol.polyval(xx,p)

punto = valor
valor = pol.polyval(punto,p)

print(int(valor), ' mpg')

plt.figure()
plt.plot(x,y,'o')
plt.plot(xx,yy,'r-')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.plot(punto,pol.polyval(punto,p),'ro')
plt.plot([punto,punto,0],[0,pol.polyval(punto,p),pol.polyval(punto,p)],'r--')
plt.axis([40,240,7,50])
#plt.show()
#%%