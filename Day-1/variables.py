print ("I'm learning Python from", 24, "December", 2025)

x= 30
y = "mr X"
z = 3.5
print (x)
print (y)
print (z)

# lets find out the types 
print (type(x))
print (type(y)) 

# Overwrite issues

x = "thirty"
X  = "Crow"
print (x)
print (X)

# camel case 
myVariableName = "John"
print (myVariableName)

# snake case
mu_variable_name = "Doe"
print (mu_variable_name)

# Pascal case
MyVariableName = "Smith"
print (MyVariableName)



#  Multiple Variables Multiple Variables

a, b, c = 5, "Hello", 7.5
print (a)
print (b)
print (c)


x=y=z= "Same Value"
print (x)
print (y)
print (z)

# Unpacking a Collection
techs = ["Python", "Java", "C++"]
a, b, c = techs
print (a)
print (b)
print (c)


# Output Variables
x = "awesome" 
y = "Python"
z= "journey"
print (x, y, z)
print (x + " " +  "looks" + y + " " + z)

a = 4
b = 5
print(a + b)

first_name = "John"
age = 36
str_age = "30"
#  print(first_name + age)
print(first_name + " is " + str(age) + " years old.")
print(first_name + " is " + str(int(str_age)) + " years old.")


# Global variabe 
x = "awesome"
def func():
  print("Python is " + x)
func()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Global var 
b = "great"
def myfunc2():
  global b
  b = "Interesting"
  print("Python is " + b)
myfunc2()
print("Python is " + b)