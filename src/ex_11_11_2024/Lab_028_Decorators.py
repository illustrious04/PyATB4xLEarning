"""
We have multiple types of decorators.
@staticmethod
@classmethod
@property
@functools.wraps

this wll be used in OOPS concepts.
"""

# Chaining Decorators.

def decorator1(func):

    def wrapper():
        print("Decorator-1")
        func()
    return wrapper()

def decorator2(func):

    def wrapper():
        print("Decorator-2")
        func()
    return wrapper()


@decorator1
@decorator2
def say_hello():
    print("Hello Decorators")




















