import numpy as np

def straight_multiplication(a, b): 
    if len(a[0]) != len(b):
        return "Wrong size" 
    p_matrix = np.zeros((len(a), len(b[0])))
    p_matrix += [[np.sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
    return p_matrix

def split(matrix):
    row, col = matrix.shape
    return matrix[:row//2, :col//2],\
                matrix[:row//2, col//2:],\
                matrix[row//2:, :col//2],\
                matrix[row//2:, col//2:]

def strassen_multiplication(a, b):
    size_base = len(a)
    if size_base == 1:  
        return a * b
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    p1 = strassen_multiplication(a11 + a22, b11 + b22)  
    p2 = strassen_multiplication(a21 + a22, b11)        
    p3 = strassen_multiplication(a11, b12 - b22)        
    p4 = strassen_multiplication(a22, b21 - b11)        
    p5 = strassen_multiplication(a11 + a12, b22)        
    p6 = strassen_multiplication(a21 - a11, b11 + b12)  
    p7 = strassen_multiplication(a12 - a22, b21 + b22)  
    c11 = p1 + p4 - p5 + p7 
    c12 = p3 + p5            
    c21 = p2 + p4            
    c22 = p1 + p3 - p2 + p6
    c_tmp = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return c_tmp
