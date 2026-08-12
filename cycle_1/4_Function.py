import math
import random

def add_numbers(a, b):
    return a + b

def greet(name):
    print("Hello Mr.", name)


greet("Swan")

result = add_numbers(10, 20)
print("Sum:", result)

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))


# Using random module
random_number = random.randint(1, 10)
print("Random number:", random_number)