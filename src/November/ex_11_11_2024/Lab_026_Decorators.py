# A Normal function.
# def test_ui():
#     print("I am testing the UI of the project")
# test_ui()

# Function with Decorator
def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the UI test case---> Start a Browser")
        func()
        print("After running the UI test case--> Close the browser")
    return wrapper()

@add_before_ui_after_ui
def ui_test():
    print("I am testing the UI")
