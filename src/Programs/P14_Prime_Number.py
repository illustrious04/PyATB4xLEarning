"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
For example, 2, 3, 5, and 7 are prime numbers.
"""

# Take user input
number = int(input("Enter your number to check if it is prime\n"))

#Check if the number is prime.

if number > 1:
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number ")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")








































































