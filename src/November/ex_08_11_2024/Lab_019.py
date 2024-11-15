# Sum of 3 numbers

def sum_of_two_numbers(a,b,c):
    return  a+b+c

result_sumOfThreeNumbers = sum_of_two_numbers(10,50, 80)
print("Sum of 3 numbers -> ", result_sumOfThreeNumbers)


def example1(a, b, c=10):
    return a+b+c
result_of_example1 = example1(10,20)
print("Result of Example 1 -> ",result_of_example1)

def example2(a, b=20, c=30):
    return a+b+c
result_of_example2 = example2(10)
print("Result of Example 2 -> ", result_of_example2)

def example3(a=5,b=10,c=15):
    return a+b+c
result_of_example3 = example3()
print("Result of Example 3 -> ", result_of_example3)

