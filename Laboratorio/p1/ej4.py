#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uo296102
#
# Created:     24/01/2024
# Copyright:   (c) uo296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
##EJERCICIO4
a = [1,2,3]
b = []
b = np.append(b,0)
b = np.append(b, a)
b = np.append(b,0)
print(b)

b1 = [0,0,0,0,0]
b1[1:4] = a
print(b1)

c = [0]
b2 = np.concatenate((c,a,c))
print(b2)
