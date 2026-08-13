import numpy as np

# 2x + y = 5
#  x +3y =6

A = np.array([
    [2,1],
    [1,3]
])

B = np.array([
    [5],
    [6]
])


x = np.linalg.solve(A,B)

print(f"Solution of the given linear is \n{x}")