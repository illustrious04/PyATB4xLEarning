# Write a program to find max between 3 numbers

num1 = int(input("Enter 1st number\n"))
num2 = int(input("Enter 2nd number\n"))
num3 = int(input("Enter 3rd number\n"))

"""if num1 > num2 and num1 > num3:
    print("Number 1 is grater")
elif num2 > num1 and num2 > num3:
    print("Number 2 is greater")
else:
    print("Number 3 is greater") """

# We can also use the max function

result = max(num1, num2, num3)
print("Max Number is ->", result)