

'''
Find if the input year is a leap year or not.
The year must be divisible by both 100 AND 400 to be a leap year, or
if it is not divisible by 100, it must be divisible by 4.
Print a message telling the user if it is leap year or not.
'''
# ---Constants
HUNDRED = 100
FOURH = 400
FOUR = 4
# ---Input
year = int(input("Enter a year: "))
# ---Calculation and Output
if (year % HUNDRED) == 0:
    if (year % FOURH) == 0:
        print(year, " is a leap year. February has 29 days")
    else:
        print(year, " is not a leap year. February has 28 days")
else:
    if (year % FOUR) == 0:
        print(year, " is a leap year. February has 29 days")
    else:
        print(year, " is not a leap year. February has 28 days")
