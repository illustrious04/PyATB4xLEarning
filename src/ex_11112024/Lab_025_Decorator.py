# Understanding Decorators in Python
"""
Decorators are a way to modify the behavior of a function or a class without changing its source code.
They are a powerful tool that allows you to wrap another function and extend its functionality,
while keeping the original function
"""


# Decorator function
# Decorator has 2 parts, Wrapper and call

def my_decorator(func): #The name of the decorator will be anything.
    def wrapper():
        print("1. Before the function is called.")
        print("2. Add Hetmet, Dashcam, Gloves, Knee Gaurds")
        func()
        print("3. After the function is called.")
        print("Secure Drive")
    return wrapper()

@my_decorator
def drive_bike():
    print("I am driving")

# Advantage: Previously drive_bike is a normal function, now added a @ annotation, (Extra Layer)

"""
Benefits of decorators:
1-> Code Reusability: Allows you to reuse the same functionality across multiple functions
without duplicating the code.
2-> Separation of Concerns: Helps in separating the code logic of functions from auxiliary concerns like
Logging, access controls etc.
3-> Enhanced Readability: Make your code more readable and maintainable by clearly separating 
different aspects of functionality

"""

































