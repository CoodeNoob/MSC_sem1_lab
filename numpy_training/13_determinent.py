import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

# det(A)=(1)(4)−(2)(3)=−2

print(f"Determinant of A is {np.linalg.det(A)}")