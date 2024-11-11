# Create a program to find the sum of 3 numbers by taking user input

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))

def sum_of_three_numbers(n1,n2,n3):
    return n1+n2+n3
result_of_three_numbers = sum_of_three_numbers(n1=num1, n2=num2,n3=num3)
we_can_also_write_like_this = sum_of_three_numbers(num1,num2,num3)
print(result_of_three_numbers)
print(we_can_also_write_like_this)