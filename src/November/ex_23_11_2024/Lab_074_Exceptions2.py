"""
# Exceptions Handling:

"""


print("------Start of the Program")

try:
    a = int(input("Enter 1st number\n")) # ValueError: invalid literal for int() with base 10: 'suyash'
    b = int(input("Enter 2nd Number\n"))
    result = a / b # ZeroDivisionError
    print(result)

except Exception as e:  # aliase= Short form
    print(e)
    print("Please check your inputs")


print("------End Of the program")

