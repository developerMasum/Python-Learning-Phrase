def my_function():
    print("Hello from a function")


my_function()


def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")

# keyword arguments


def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)


my_function(animal="Cat", name="Buddy")

# --------------------------------


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# *args and **kwargs
# allows a function to accept a variable number of arguments.

def child_functions(*kids):
    print("The youngest child is " + kids[2])


child_functions("Emil", "Tobias", "Linus")


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")

# ---------------------------------


def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


add = my_function(1, 2, 3, 4, 5)
print("Total:", add)


x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)

# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions(from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)


outer()
print("Global:", x)
