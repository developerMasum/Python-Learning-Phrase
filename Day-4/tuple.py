# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
print(len(thistuple))
# comma is must for tuple with single value
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (True, False, False)

print(tuple1[0])
print(tuple2[-1])
print(tuple3[1:2])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print(thistuple[5:])
if "bana" in thistuple:
    print("Yes, 'banana' is in the fruits tuple")

# update
#  change value of tuple by converting it to list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# add value to tuple by converting it to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


tuple = ("mango", "orange", "grapes")
(x, y, z) = tuple
print(tuple)
print(x)
print(y)
print(z)


# Using Asterisk*
# used for rest of the values as list as asterisk

x = ("car", "bike", "bus", "train", "aeroplane")
(a, b, *c) = x

print(a)
print(b)
print(c)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print(fruits * 2)  # duplicates the tuple\
print(fruits + x)  # concatenation of tuples

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
repeat = number * 3

print(repeat)  # prints the tuple repeated 3 times
print(repeat.count(3))  # counts occurrences of 3 in the tuple
print(repeat.index(7))  # finds the first index of 7 in the tuple
