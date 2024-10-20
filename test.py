import numpy as np
import scipy

def swap_rows(mat, i, j):
    n = len(mat[0])
    for k in range(n):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp

def gauss(mat):
    swap_count = 0
    mat = np.array(mat, dtype=float)
    m = len(mat)
    n = len(mat[0])
    h = 0
    k = 0
    while h < m and k < n:
        i_max = np.argmax(np.abs(mat[h:, k])) + h
        if mat[i_max, k] == 0:
            k += 1
        else:
            if i_max != h:
                swap_rows(mat, h, i_max)
                swap_count += 1
            for i in range(h+1, m):
                f = mat[i, k] / mat[h, k]
                mat[i, k] = 0
                for j in range(k+1, n):
                    mat[i,j] = mat[i,j] - mat[h,j] * f
            h += 1
            k += 1
    return mat, swap_count
            
    
            
A = np.array([
    [0, 0, 2, 1, 2],
    [0, 1, 0, 2, -1],
    [1, 2, 0, -2, 0],
    [0, 0, 0, -1, 1],
    [0, 1, -1, 1, -1]
])

m =len(A)
A = gauss(A)[0]

for i in range(m-1, -1, -1):
        j = np.argmax(np.abs(A[i]))
        A[i] /= A[i][j]
        for k in range(i-1, -1, -1):
            A[k] -= A[i] * A[k][j]
print(A)