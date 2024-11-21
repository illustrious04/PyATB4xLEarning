# Constructor
"""
1- It is a special function in the class with the name __init__()
2- it will be automatically called when you create an object.
3- Constructors does not return anything.
"""

class Dog:
    name = None
    # Default constructor
    def __init__(self):
        print("I am a Default constructor and will be automatically called when you create an object")
    def sleep(self):
        print("Dog is sleeping")
dog1 = Dog()
dog1.sleep()
dog1.name = "Mow"
print(dog1.name)



