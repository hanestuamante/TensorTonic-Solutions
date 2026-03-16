import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    result = np.zeros((cols, rows))
    for i in range(rows):
        for j in range(cols) :
            result[j][i] = A[i][j]

    return result
    
    
   
