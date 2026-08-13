import numpy as np

matrix = [
    [1,2,3],
    [5,6,7]
]

matrix_1 = [
    [1,2,3],
    [5,6,7]
]


numpy_matrix= np.array(matrix)
numpy_matrix_1= np.array(matrix_1)

print(f"Sum of two matrix is \n{numpy_matrix+numpy_matrix_1}")
print(f"Sub of two matrix is \n{numpy_matrix-numpy_matrix_1}")
print(f"Multiply of two matrix is \n{numpy_matrix@numpy_matrix_1.T}")
print(f"Transpose of the Matrix is {numpy_matrix_1.T}")

# Trace is the sum of the main diagonal
print(f"Trace of the Matrix is {np.trace(matrix)}")