# for loop through a list

list = ["apple", "banana", "cherry", "date"]
for x in list:
    print(x)


animals = ["cow", "tiger", "lion"]
for i in range(len(animals)):
    print(animals[i])


# while loop through a list

fruits = ["grapes", "orange", "kiwi", "pear"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

    thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
