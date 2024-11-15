class dog: # Class name will always start from Capital letters.
    name = "None"
    breed = "None"
    color = "None"

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def eat(self, food):
        print(food)


dog1 = dog
dog1.name = "Chow"
print(dog1.name)
dog1.color = "White"
print(dog1.color)

print("----------------------------------")
dog2 = dog
dog2.name = "Mow"
dog2.color = "Black"
print("Dog2 has name =", dog2.name + " , And His Color is " + dog2.color)


