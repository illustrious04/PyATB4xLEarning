# Calculator with Non parametrize constructor

class Calculator:
    # def __init__(self):
    #     print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a , b):
        return a - b

    def mul(self, a , b):
        return a * b

    def div(self, a , b):
        return a / b

calculation = Calculator()
a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))

output_sum = calculation.sum(a, b)
output_sub = calculation.sub(a , b)
output_mul = calculation.mul(a , b)
output_div = calculation.div(a , b)

print(output_sum, output_sub , output_mul, output_div)
