import numpy as np

matrix = [
    [1,2,3],
    [5,6,7]
    # [8,9,10]
]

matrix_1 = [
    [1,2,3],
    [5,6,7]
]

eig_matrix = [
    [1,2],
    [3,4]
]


numpy_matrix= np.array(matrix)
numpy_matrix_1= np.array(matrix_1)

print(f"Sum of two matrix is \n{numpy_matrix+numpy_matrix_1}")
print(f"Sub of two matrix is \n{numpy_matrix-numpy_matrix_1}")
print(f"Multiply of two matrix is \n{numpy_matrix@numpy_matrix_1.T}")
print(f"Transpose of the Matrix is {numpy_matrix_1.T}")

# Trace is the sum of the main diagonal
print(f"Trace of the Matrix is {np.trace(matrix)}")


# EiganValues and Eigan Vectors
values, vectors = np.linalg.eig(eig_matrix) # matrix must be square

