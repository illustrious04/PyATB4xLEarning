"""
Write a program that prints number from 1 - 100.
Loop for however for multiple of 3,
Print "Fizz" instead pf number,
and for multiple of 5, print "Buzz"

For number that are multiple of both 3 and 5, print "FizzBuzz"
"""

for i in range(1,101,1):
    if i%3 ==0 and i%5==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("FIzz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
