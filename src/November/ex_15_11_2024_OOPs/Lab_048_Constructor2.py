# Constructor with argument
from queue import PriorityQueue


class cat:
    name = None

    # Constructor with parameter
    def __init__(self, name, age):
        print("Called object is created")
        self.name = name
        self.age = age

    def sleeping(self):
        print("Who is sleeping=> " + self.name + " Whose age is => " + str(self.age))

cat1 = cat("Billi", 10)
print(cat1.name)
print(cat1.age)
cat1.sleeping()


print("---------------------------------------------")
cat2 = cat("Cat2",18)
cat2.sleeping()
