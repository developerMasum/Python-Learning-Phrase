# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

import datetime

x = datetime.datetime.now()
print(x)


x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
