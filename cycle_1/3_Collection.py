# List operations
numbers = [10, 20, 30, 40]

print("List:", numbers)
numbers.append(50)
print("After append:", numbers)
numbers.remove(20)
print("After remove:", numbers)
print("First element:", numbers[0])


# Tuple operations
fruits = ("Apple", "Banana", "Orange")

print("\nTuple:", fruits)
print("First element:", fruits[0])
print("Length:", len(fruits))
print("Contains Banana:", "Banana" in fruits)


# Dictionary operations
student = {
    "name": "Swan Htet",
    "age": 23,
    "course": "Computer Science"
}

print("\nDictionary:", student)
print("Name:", student["name"])

student["age"] = 21
student["university"] = "University of Kerala"

print("After update:", student)
print("Keys:", student.keys())
print("Values:", student.values())


# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

set1.add(7)
print("After adding 7:", set1)