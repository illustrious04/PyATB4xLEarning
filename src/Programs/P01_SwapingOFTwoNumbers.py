#Swapping of 2 numbers
num1 = input("Enter num1 value")
num2 = input("Enter num2 value")

print("num1 before swapping", num1)
print("num1 before swapping", num1)

#Approch 1: With using Temperory variable
"""
tmp = num1     #10
num1 = num2       #20
num2 = temp
""" #10

# Approch 2: Without using temp variable

num1,num2 = num2,num1
print("Value of num 1 after swapping", num1)
print("Value of num2 after swapping", num2)