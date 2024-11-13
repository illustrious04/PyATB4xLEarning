# Dictionary => Dict
"""
It is most used.
it is      key =   value pair
Example : name = "Suyash
We can have multiple key value pairs.

Dict is unordered collection of list
-> It will be mostly used in API Automation testing
-> Looks like Json format.
"""
employee_information = {
    "name": "Suyash",
    "age": 33,
    "ID": "TVE_317",
    "Designation": "QA Automation Lead",
    "Company": "Techvalens"

}

print(employee_information)
print(employee_information["name"])

# We can also change the value as well
employee_information["age"] = 100
print(employee_information)

print("------------------Another way of creating dict--------------------------")

# Try to avoid this way
new_employee_info = dict(name="suyash", age=33, id="TVE-317")
print(new_employee_info)
