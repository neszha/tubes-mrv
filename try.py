# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
# n = int(input('Enter number of unknowns: '))
n = 2

# Making numpy array of n x n+1 size and initializing
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
# print('Enter Augmented Matrix Coefficients:')
# for i in range(n):
#     for j in range(n+1):
#         a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
#
# print(a)
a = np.array(([1,2,3], [4,5,6]))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]

        for k in range(n+1):
            a[j][k] -= ratio * a[i][k]

# print(a)
# # Back Substitution
print(a)

print('before', x)
x[n-1] = a[n-1][n]/a[n-1][n-1]
print('after', x)

for i in range(n-2,-1,-1):
    x[i] = a[i][n]

    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]

    x[i] = x[i]/a[i][i]

print(x)
# # Displaying solution
# print('\nRequired solution is: ')
# for i in range(n):
#     print('X%d = %0.2f' %(i,x[i]), end = '\t')
