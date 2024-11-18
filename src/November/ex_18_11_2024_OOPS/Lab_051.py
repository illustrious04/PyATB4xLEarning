# Take userinput and create a class in Pythin.

class Person:
    def __init__(self):
        self.name = input("Enter your name\n")
        self.age = input("Enter your age\n")
        self.phonenumber = input("Enter your Phone number\n")
        self.profile = input("Enter your Phone Profile\n")
        print("-" * 30)

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone Number is {self.phonenumber}")
        print(f"Profile is {self.profile}")


# Create an object

person1 = Person()
# Call the display function
person1.display_information()
