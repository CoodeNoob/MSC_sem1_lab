import numpy as np

one_d_array = np.array([1,2,3,4,5,6])
two_d_array = np.array([
    [1,2,3],
    [4,5,6]
])


print(f"Shape of each array is {one_d_array.shape} & {two_d_array.shape} ") # Row and Columns
print(f"Size of each array is {one_d_array.size} & {two_d_array.size}") # total elements
print(f"Dimension of each array is {one_d_array.ndim} & {two_d_array.ndim}") # dimension
print(f"Datatype of each array is {one_d_array.dtype} & {two_d_array.dtype}")

# indexing
print(f"Indexing of first element of each array is {one_d_array[0]} & {two_d_array[0][1]}")

# Reshaping
print(f"Reshaping the each array: \nFrom\n{one_d_array}\nTo\n{one_d_array.reshape(2,3)} & \n From\n{two_d_array}\nTo\n{two_d_array.reshape(-1)}")

