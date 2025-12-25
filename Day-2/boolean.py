# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.


print(5>3  )  # True
print(3>11 )  # False

print(bool("Hello"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(""))
print(bool(0))
print(bool([]))

def myFunction() :
  return True

print(myFunction())