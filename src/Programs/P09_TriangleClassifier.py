"""
Write a program that classifies a triangle based on its side length
Given three inputs values respresenting the length of the sides,
determine if the triangle is Equilateral (All side are equal)
Isosceles (Exactly 2 sides are equal) or scalene (No sides are equal.
use if-else statement to classify the triangle.
"""

#Get the user input for all the 3 sides of the triangle.

side1 = float(input("Enter 1st side\n"))
side2 = float(input("Enter 2nd side\n"))
side3 = float(input("Enter 3rd side\n"))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # clasify the triangle
   if side1 == side2 == side3:
       print("triangle is equilateral.")
   elif side1 == side2 or side1 == side3 or side2 == side3:
       print("Triangle is Isosceles.")
   else:
       print("Triangle is Scalene")






