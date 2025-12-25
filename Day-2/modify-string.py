x = "   This is Modified String , as I need to modify it.   "
print(x)

print(x.upper())  # Convert to uppercase
print(x.lower())  # Convert to lowercase
print(x.strip())  # Remove whitespace from both ends
print(x.replace("Modified", "Replaced"))  # Replace substring
print(x.split())  # Split string into a list


# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)  
d = a + " " + b
print(d)


# String Formatting
name = "Alice"
age = 30
x = "My name is " + name + " and age is " + str(age)
print(x)
# F-Strings
# Using f-strings (Python 3.6+)

Y = f" {name} is {age} years old."
print(Y)


price = 49
quantity = 3
text = f" price {price:.4f} dollars."
print(text)
math = f" the total price os {price * quantity} dollars."
print(math)


# ------------------- escape characters -------------------
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)