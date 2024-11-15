class Person:
    # Attributes

    id = "none",
    name = "none"
    age = "none"
    email = "none"
    height = "none"
    weight = "none"
    gender = "none"
    address = "none"
    phone_number = "none"

    #Behaviour
    def talk(self): #self means this in java, it is a 1st argument in every behaviour. function with No argument.
        print("I can talk")

    def sleep(self, name): #Function with argument and no return type.
        print("I can sleep", name)

    def sleep2(self, name): # Function with Argument and return type = none
        print("", name)
        return None

    def walk(self): # No argument and no return type.
        print("I can walk")

# create an object of the class
# ObjectRef = ClassName() -> Object

employee = Person()
employee.name = "Suyash"
print(employee.name)

hr = Person()
hr.weight = 90
print(hr.weight)



















