# Calculator with parametrize  constructor
from src.Programs.P06_MaxBetween3Numbers import result


class Calculator:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

calculation = Calculator(4, 9)
output = calculation.sum()
print(output)



