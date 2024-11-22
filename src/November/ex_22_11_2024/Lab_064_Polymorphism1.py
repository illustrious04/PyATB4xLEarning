"""
# Polymorphism:
* OOPs Concept.
* Objects -> Many forms.
* Behavior -> Based on who is calling.
* Allows object of different classes to be treated as object of common super classes.
* Archived by using 2 methods:
1- Method Overriding
2- Method Overloading
"""
"""
# Method Overriding:
# Says that the Child or Sub-class can have the same name Method as the Parent or super class.
* Child always override the parent function.
* Super means call my parent method.
"""

class Shape:
    def area(self):
        print("Print the Area of the shape")

class Rectangle(Shape):   # Is-A relationship
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


class Circle(Shape):  # Hierarchical Inheritance
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3,4)
print(shape1.area())  # It will call line number 25 1st because the local method has always the 1st priority.

shape2 = Circle(10)
print(shape2.area())


