"""
=> Multiple Inheritance.
* A child class inherits from multiple parent classes
* Diamond Problem: If the parent classes has the same name functions and when that function is called by
the child class, the whichever the class is in 1st position, it will call.
* This problem is not solved in JAVA, buy python has resolved this problem.
* The solution is called as "MRO" - Method Resolution Order.
"""

class Father:
    def father_money(self):
        return "This is Father Money"

    def home(self):
        return "This is father Home"

class Mother:

    def mother_money(self):
        return "This is Mother's Money"

    def home(self):
        return "This is Mother's Home"

class Son1(Mother, Father):
    pass

class Son2(Father, Mother):
    pass

son1 = Son1()
print(son1.home())


son2 = Son2()
print(son2.home())