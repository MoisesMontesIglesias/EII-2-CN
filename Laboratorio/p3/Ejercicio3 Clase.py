#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      uo296102
#
# Created:     07/02/2024
# Copyright:   (c) uo296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sustitucion_regresiva(A,b):
    size = A.shape[0]
    x = np.zeros(size)
    x[size-1] = b[size-1]/A[size-1,size-1]
    for i in range(size-2,-1,-1):
        x[i] = (b[i]-A[i,j+1]*x[i+1])/A[i,i]

    return x


x = sustitucion_regresiva(A,b)
print( x )
