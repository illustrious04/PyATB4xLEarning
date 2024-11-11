# Lambda Expression

"""
A lambda is an anonymous function that returns some form of data.

"""

def triple_mult(num):
    return num ** 3

output = triple_mult(10)
print(output)

# Instead of this we can also write like this

# def triple_mul_new(num):
#     return num ** 3

output_new = lambda num: num ** 3
print("Lamda Calculation", output_new(10))






























