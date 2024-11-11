# Lambda Expression
import math


def give_power(num):
    return math.pow(num,2)
op1 = give_power(10)
print(op1)

# converting the above program to Lambda function with taking user input

op2 = lambda : math.pow(int(input("Enter the Number\n")), 2)
print(op2())























