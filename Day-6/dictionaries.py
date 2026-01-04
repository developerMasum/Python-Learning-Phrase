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
