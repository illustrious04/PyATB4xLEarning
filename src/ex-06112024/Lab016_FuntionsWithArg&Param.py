# All About functions.
# Functions re of 4 types
# 1-> No- Return type
# 2-> No- Return type & with Argument
# 3-> No return type and with default argument
# 4-> Argument + Return type.

# 1->  No Return type
def no_return_type_arg():
    print("ABC")
result = no_return_type_arg()
print(result)  # This will return None


# 2-> No- Return type & with Argument
def greet_by_name(name):
    print("Hello", name)

greet_by_name("Suyash")


# 3-> No return type and with default argument
def say_hello_to_default_args(name = "Default argument Suyash"):
    print("Hello", name)
say_hello_to_default_args()

# We can also give multiple arguments
def multiple_args(name1 = "Tiger", name2 = "Lion", name3 = "Cheetah"):
    print("Hello Multi Args", name1, name2, name3)
multiple_args()

# 4-> Argument + Return type.
def sum_of_two_numbers(num1,num2):
    return num1+num2
result = sum_of_two_numbers(num1=34, num2=44)
print(result)

#With default Arguments
def sum_of_two_numbers_with_default(num1=44, num2=200):
    return num1+num2
default_result = sum_of_two_numbers_with_default()

print(default_result)