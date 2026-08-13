import numpy as np

# creating the generator
rng = np.random.default_rng(seed=42)

# random number between 0 and 1
print(rng.random())

# size array of rabdom number
print(rng.random(4))


# 2x3 array (given size with tuple)
print(rng.random((2,3)))

# random uniform generation 
print(rng.uniform(0,10,size=5))

# generate only random integer [0,10]
print(rng.integers(10))
