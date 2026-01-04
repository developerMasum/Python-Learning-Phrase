# function.py
# check leap year or not
year = int(2024)


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    result = is_leap_year(year)
    if result:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
