import numpy as np

# A^-1 = 1/|A| * adj(A)

# def get_inverse_matrix(matrix):
#     det = np.linalg.det(matrix)
#     adj = ""
#     pass

# def get_cofactor_matrix(matrix):
#     pass


given_matrix = [
    [1,0,5],
    [2,1,6],
    [3,4,0]
]

print(f"Inverse of given matrix is \n{np.linalg.inv(given_matrix)}")

