"""
* Encapsulation
> You can bind Data Variables with the methods.
> Hide the data members (Class variable, Instance Variable). By using only the methods.
>
"""

"""
1= Public Variable: 
* Public can be access from anywhere. 
2= Private Variable:
* Scope of private is only within the class
* Defined by __
3= Protected variable: 
* It is available within the same python package.
* Members are intended for internal use within the class and its subclass.
* Scope of protected is within the same package.
* Defined by _

"""

class Myclass:
    public_var = "I am public instance variable"
    _protected_var = "I am Protected Variable"
    __private_var = "I am Private instance variable"


obj = Myclass()
print(obj.public_var)
# print(obj.__private_var) We can not access the private variable
print(obj._protected_var)
