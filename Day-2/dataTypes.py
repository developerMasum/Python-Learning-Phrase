# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Example usages of different data types in Python

# String
name = "Alice"
print("Name:", name, "| Type:", type(name))

# Integer
age = 30
print("Age:", age, "| Type:", type(age))
print("age in float:", float(age), "| Type:", type(float(age)))
print("age in complex:", complex(age), "| Type:", type(complex(age)))

# list
sequence = [1, 2, 3, 4, 5]
print(sequence,"|type" , type(sequence))

# tuple
coordinates = (10.0, 20.0)
print(coordinates,"|type" , type(coordinates))

# range
numbers = range(20)
print(numbers,"|type" , "|display contents", list(numbers), "|type", type(numbers))
# dict
person = {"name": "Bob", "age": 25}
print(person,"|type" , type(person))
# set
names = {"Alice", "Bob", "Charlie"}
print(names,"|type" , type(names))

# random numbers
import random

print(random.randrange(1, 10000))
