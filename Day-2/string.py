a = "Hello, World!"
print(a)

x= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea"""
print("this is biggg text", x)

# Strings are Arrays
b = "Hello, World!"
print(b[8])

# Looping Through a String
for x in "hey python":
  print(x)

#   length
print("length of string" ,len(b))

# check  string  
z = "Life is beautiful with python"
print("string or not  : ", "python" in z)

if "python" in z:
  print("yes, 'python' is present")

  if "java" not in z:
    print("no, 'java' is not present")
