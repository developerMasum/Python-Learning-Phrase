# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


# ------------------------------------------------------------------

x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(x)

point = x["brand"]
print(point)

# add new item
x["color"] = "red"
print(x)

print(len(x))

# get
y = x.get("model")
print(y)
# get keys
x = x.keys()
print(x)
b = {
    "model": "Fiat",
    "year": 2020
}
# get values
z = b.values()
print(z)

thisdict = dict(name="John", age=36, country="Norway")

print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)


# ------- Day-5/sets.py -------
dict = {"dinner": "pasta", "lunch": "burger", "breakfast": "eggs"}
for x in dict:
    if x == "lunch":
        break
    elif x == "breakfast":
        continue

    print("vanuu has taken her:", x)
    if x == "dinner":
        print("Farhan also take his dinner:", dict[x])


# nested
# {

    child1 = {
        "name": "Emil",
        "year": 2004
    }
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
