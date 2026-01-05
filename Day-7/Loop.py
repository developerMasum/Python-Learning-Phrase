# Python has two primitive loop commands:

# while loops
# for loops


# while condition loop
i = 1
while i <= 6:
    print(i)
    i += 1
print("While loop ended")


i = 2
while i <= 100:
    print(i)
    if i == 50:
        break
    i += 2
print("While loop with break ended")


# continue means to skip the current iteration and move to the next one.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # print(fruit)
    # if fruit == "banana":
    #     break
    if fruit == "apple":
        continue
    print(fruit)

for x in range(22):
    print(x)
