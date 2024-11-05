import numpy as np
from scipy.linalg import solve

A = np.array([
    [1, 1/2, 1/3, 1/4, 1/5],
    [1/2, 1/3, 1/4, 1/5, 1/6],
    [1/3, 1/4, 1/5, 1/6, 1/7],
    [1/4, 1/5, 1/6, 1/7, 1/8],
    [1/5, 1/6, 1/7, 1/8, 1/9]
])

b = np.array([5,4,3,2,1])

def lu(mat):
    n = len(mat)
    L, U = np.zeros((n,n)), np.zeros((n,n))

    for i in range(n):
        for k in range(i, n):
            sum_ = 0
            for j in range(i):
                sum_ += (L[i][j] * U[j][k])
            U[i][k] = mat[i][k] - sum_

        for k in range(i, n):
            if (i == k):
                L[i][i] = 1 
            else:
                sum_ = 0
                for j in range(i):
                    sum_ += (L[k][j] * U[j][i])
                L[k][i] = (mat[k][i] - sum_) / U[i][i]
    return L, U

def dokladnosc_maszynowa(x_0):
    x = x_0
    while x + 1 != 1:
        x /= 2
    return x
            
def iteracyjne_poprawianie_rozwiazan(A, b):
    L,U = lu(A) #rozkład LU
    y = solve(L, b) #rozwiązujemy za pomocą LU
    x = solve(U, y)
    Ax = np.dot(A, x)
    r = b - Ax #reszty
    u = dokladnosc_maszynowa(1)
    while np.linalg.norm(r,np.inf) < np.linalg.norm(Ax, np.inf) * u:
        print(1)
        delta_x = solve(A, r)
        x += delta_x
        r = b - np.dot(A, x)
    return x

print(iteracyjne_poprawianie_rozwiazan(A, b))