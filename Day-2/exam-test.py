# ===============================
# PYTHON PRACTICE QUESTIONS
# Topics: Numbers, Casting, Strings, Booleans
# ===============================


# Q1: Convert the string "25" into an integer and add it with 5.
# Print the result.

x = "25" 
result = int(x)+5
print(result)


# Q2: Given two numbers x = 7 and y = 2
# Print:
# 1) Integer division result
# 2) Normal division result
# 3) Remainder
x = 7
y = 2
print(x // y)  # Integer division
print(x / y)   # Normal division
print(x % y)   # Remainder


# Q3: Convert and print the data types:
# a) 10 to float
# b) 9.8 to int
# c) "100" to int

a = float(10)
b = int(9.8)
c = int("100")
print(a)
print(b)
print(c)

# Q4: Given the string "PythonProgramming"
# Print:
# 1) First 6 characters
# 2) Last 6 characters
# 3) Every second character
s = "PythonProgramming"
print(s[:6])        # First 6 characters
print(s[-6:])       # Last 6 characters     
print(s[::2])       # Every second character


# Q5: Reverse the string "Developer"
# Expected output: repoleveD
s = "Developer"
reversed_s = s[::-1]
print(reversed_s)


# Q6: Convert the string "i love python" into "I Love Python"
a="i love python"
b = a.title()
print(b)

# Q7: Count how many times the letter "a" appears in "banana"
count = "banana".count("a")
print(count)


# Q8: Check whether the string "python123" contains only alphabets
# Print True or False
x = "python123"
print(x.isalpha())


# Q9: Replace all spaces with "_" in the string
# "Python is easy to learn"
text = "Python is easy to learn"
modified_text = text.replace(" ", "_")
print(modified_text)


# Q10: Using f-string, print the sentence:
# My name is Farhan and I am 22 years old.
# Use variables name = "Farhan", age = 22
name = "Farhan"
age = 22
x = f" My name is {name} and I am {age} years old."
print(x)



# Q11: Check whether the number 15 is greater than 10
# AND less than 20. Print the result.
print(15 > 10 and 15 < 20)

# Q12: Check whether an empty string "" returns False using bool()
print(bool(""))

# Q13: Write code to check if a number is even or odd.
# Use number = 17
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q14: Check whether "Python" is equal to "python"
# Print True or False
print("Python" == "python")


# Q15 (Challenge): Given price = "500" and tax = 10
# Convert price to integer and calculate total price after tax.
price = "500"
tax = 10
total_price = int(price) + (int(price) * tax / 100)
print(total_price)




# 🏆 Final Score

# Total Marks: 22.5 / 24 ⭐⭐⭐⭐⭐
# Performance: Excellent