"""
# Exceptions Handling:

# try, except and finally.
# Multiple except
"""


 # Exception with else condition
try:
    a = int(input("Enter 1st number\n")) # ValueError: invalid literal for int() with base 10: 'suyash'
    b = int(input("Enter 2nd Number\n"))

    result = a / b # ZeroDivisionError

except ValueError as e:
    print("Value Error")

except ZeroDivisionError as zde:
    print("Zero Division Error, dont use number 2 as zero.")
else:
    print(f"Result is {result}")
finally:
    print("This code will always be executed!")

