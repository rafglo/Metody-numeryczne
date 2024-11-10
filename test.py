import numpy as np

def generate_matrix(n):
    mat = np.zeros((n,n))
    for i in range(n):
        mat[i][i] = 4
        if i - 1 >= 0:
            mat[i][i-1] = -1
        if i + 1 < n:
            mat[i][i+1] = -1
        mat[0][-1] = 1
        mat[-1][0] = 1
    return mat
                     

def ldu(mat):
    n = len(mat)
    l, d, u = mat, mat, mat
    for i in range(n):
        for j in range(n):
            if j > i:
                l[i][j] = 0
                d[i][j] = 0
            if j == i:
                l[i][j] = 0
                u[i][j] = 0
            if i > j:
                u[i][j] = 0
                d[i][j] = 0
    return l, d, u 

a = generate_matrix(5)

print(ldu(a))