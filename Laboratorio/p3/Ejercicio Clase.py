#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uo296102
#
# Created:     07/02/2024
# Copyright:   (c) uo296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

def diagonalizar_por_debajo(A):
    size = A.shape[0]
    if(A.shape[0] != A.shape[1]):
        print("Warning! sizes of the matrix")
        return

    for i in range(0,size):
        for j in range(i+1,size):
            coef = A[j,i]/A[i,i]
            A[j,:] = A[j,:] - coef*A[i,:]
    return A

n = 7
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1+A2+A2.T
AD= diagonalizar_por_debajo(A)
print(AD)








