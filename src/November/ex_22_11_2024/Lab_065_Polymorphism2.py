# Method Overriding:
# Parent attribute and behavior can be accessed by using super() keyword

class Father:

    father_attribute = 10

    def home(self):
        print("Father ka Ghar: 1 BHK")

class Son(Father):
    son_attribute = 20

    def home(self,):
        print("Son Ka Ghar: 3 BHK")
        super().home() # Fathers Home
        print(super().father_attribute) # Father Attribute.


son = Son()
print(son.home())
print(son.father_attribute)
