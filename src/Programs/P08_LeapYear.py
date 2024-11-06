"""Leap Year
Create a program that determines whether a given year is leap year or not
A leap year is divisible by 4 but not by 100 unless it is also divisible by 400
use if-else statement to make this determination

"""

"""Logic 
Divisibility by 4: A year is considered a leap year if it is divisible by 4. 
So, year % 4 == 0 checks if there is no remainder when the year is divided by 4.

Divisibility by 100: If a year is divisible by 4, it is a candidate to be a leap year. 
However, if the year is also divisible by 100 (like 1900), it is not a leap year unless it is also divisible by 400. 
This step ensures that years like 1700, 1800, and 1900 are not treated as leap years.

Divisibility by 400: This is a special case for century years. If a year is divisible by 400, 
it is indeed a leap year. For instance, 1600 and 2000 are leap years, while 1700, 1800, and 1900 are not.

"""
# Get the year from the user

year = int(input("Enter  year: \n"))

#Check if the year us a leap year.
if year % 100 == 0 and year % 400 == 0:
    print("Entered year is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Entered year is a leap year")
else:
    print("Entered year {} is not a leap year".format(year))



































