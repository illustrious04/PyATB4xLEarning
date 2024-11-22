"""
=> Multi-Level Inheritance.
* A class inherits from another class, and then another class inherits from it (chain of inheritance)
"""

class Grand_father:
    property = "4000 Sqft Land"

    def grand_home(self):
        print("Grand Home in Village")

    def gold(self):
        print("2 KG Gold")

class Father(Grand_father):
    property = "1500 sqft plot"

    def parentHome(self):
        print("2BHK Flat")

class Son(Father, Grand_father):
    print("I am son and I has: ")

# Grand father Object
G_F = Grand_father()
print(G_F.property)

# Father Object
F = Father()
print(F.gold())

# Son Object
S = Son()
print(S.property)
print(S.parentHome)



