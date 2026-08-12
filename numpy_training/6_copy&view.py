import numpy as np

arr = np.array([1,2,3,4,5])

# x = arr.copy()
x = arr.view()
y = arr.copy() # no none

arr[0] = 42

print(arr)
print(x)


print(f"base of x is {x.base}")
print(f"base of y is {y.base}")

# checking the base using .base

