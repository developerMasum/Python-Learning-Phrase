# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# ------------------------------- example code -------------------------------

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# decending = True = REVERSE = TRUE
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key=str.lower)
print(thislist)


x = ["apple", "banana", "cherry"]
y = x.copy()
print(y)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# join lists uses append, extend or + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
