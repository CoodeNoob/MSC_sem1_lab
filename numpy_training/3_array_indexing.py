import numpy as np

array = np.array([1, 2, 3, 4], ndmin=1)

print(f"Indexing the first element of th numpy array {array[0]}")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# negative indexing ဆိုတာ အနောက််ကနေ ယူတာ

print('Last element from 2nd dim: ', arr[1, -1])