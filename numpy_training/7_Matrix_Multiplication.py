import numpy as np

array1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# print(f"Matrix multiplication is:\n{np.matmul(array1, array2.T)}")
print(f"Multiplication using @ is:\n{array1 @ array2.T}")