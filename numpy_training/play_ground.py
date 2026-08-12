import numpy as np

arr = np.array([1,2,3,4,5])
arr_1 = np.array([3,4,5,6,4])

print(f"Sum of two numpy array is {arr+arr_1}")
print(f"Sub of two numpy array is {arr-arr_1}")
print(f"Multiply of two numpy array is {arr*arr_1}")


two_d_array = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(two_d_array.shape) # row and columns
print(two_d_array.ndim)
print(two_d_array.size) # total element
