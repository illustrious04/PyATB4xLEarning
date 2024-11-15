"""
Create an employee class with attributes (id,name,age, phone number, address).
With the constructor which will set the values,
Ask the user about the information for E1 and E2 and print the details with print employee function.
"""

class Employees:
    def __init__(self, id, name, age, phone_number, address):
        self.id = id
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.address = address

    def print_employee(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee Phone Number: {self.phone_number}")
        print(f"Employee address: {self.address}")
        print("-" * 30)

#Function to collect user details
def get_employee_details():
    id = input("Enter Your id ")
    name = input("Enter your name ")
    age = input("Enter your age\n")
    phone_number = input("Enter your phone number ")
    address = input("Enter your address ")
    return Employees (id,name,age,phone_number,address)

#Get details from Employee 1 and Employee 2

print("Enter the details of Employee 1")
employee1 = get_employee_details()

print("Enter the details of Employee 2")
employee2 = get_employee_details()

# Print Details of Employee 1 and Employee 2

print("\nEmployee 1 details")
employee1.print_employee()

print("\nEmployee 2 details")
employee2.print_employee()

