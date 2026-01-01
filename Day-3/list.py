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

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])



# Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# extend 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop method
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

# remove last item by pop 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del keyword

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# delete all
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # this will raise an error because the list no longer exists

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)