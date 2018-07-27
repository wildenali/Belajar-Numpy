import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])
print(A)
print(Y)

A_inv = np.linalg.inv(A)

# Menyelesaikan Persamaan LINEAR
X = np.dot(A_inv,Y)
print(X)


# Cara Lain
X2 = np.linalg.solve(A,Y)
print(X2)
