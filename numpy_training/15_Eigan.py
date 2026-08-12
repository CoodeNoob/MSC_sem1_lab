import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])


print(f"Eigan value of A is {np.linalg.eig(A)}")