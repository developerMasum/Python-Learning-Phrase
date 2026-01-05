# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


a = 100
b = 200
if a < 150 and b < 250:
    print("Both conditions are True")

a = 100
b = 200
if a > 150 or b < 250:
    print("At least one condition is True")

a = True
if not a:
    print("a is False")
else:
    print("a is True")
