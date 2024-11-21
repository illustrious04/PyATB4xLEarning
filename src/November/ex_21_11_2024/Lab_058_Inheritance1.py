"""
* Inheritance:
-> Acquires the properties and behavior of other class
-> Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
This promotes code reuse and scalability
-> Types:
a) Single Inheritance
b) Multiple Inheritance.
c) Multi-level Inheritance
d) Hybrid Inheritance.
e) Heiraricle Inheritance.
"""

# Single Inheritance.

class Father:
    key = "2BHK"

    def father_car(self):
        print("This is Father's car" , "Alto")



class Son(Father):   # There is not extend keyword in Python.
    key2 = "3BHK"

    def home(self):
        print("Home of Son")

    def bike(self):
        print("Bike of the Son")




# Father Object
obj_father = Father()
# obj_father.bike() Father class can not access the properties of son class.
obj_father.father_car()

obj_son = Son()
obj_son.father_car()
print(obj_father.key) # Son class can access the properties of father class.

