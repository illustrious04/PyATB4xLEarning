# Write a python program to calculate the area of a circle given its radius using the formula
# take pai as 3.14
# A = π r²
import math
radius = float(input("Enter the radius of the circle\n"))
print(radius)

print(math.pi)

area = math.pi * math.pow(radius, 2)
print("Area of the circle is -> ", area)
print(f"Area10 of the circle is -> , {area:.2f}")