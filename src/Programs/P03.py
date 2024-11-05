# Take 2 number from user input and check 1st number is > , < or = to 2nd number

num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))

if num1 > num2:
    print("1st number is greater than 2nd number ")
elif num1 < num2:
    print("1st number is less than 2nd number")
else:
    print("Both numbers are same")
