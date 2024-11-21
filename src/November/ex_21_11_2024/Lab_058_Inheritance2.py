"""
Single Inheritance
"""

class Parent():
    Gold = "2K"
    Silver = "5KG"

    def home(self):
        print("Parent has 2BHK Home!")

    def car(self):
        print("Parents has Alto car!")

class Child(Parent):

    def child_home(self):
        print("Child has 3BHk house")

    def child_car(self):
        print("Child has Kia")

parent_obj = Parent()
parent_obj.car()


child_obj = Child()
child_obj.home()

