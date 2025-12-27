thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
thislist = list(("apple", "banana", "cherry"))
print(thislist)

mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# range of index 
print(len(thislist[1:3]))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# change list items

list1 = ["apple", "banana", "cherry"]
list1[0] = "blackcurrant"
print(list1)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# partial change