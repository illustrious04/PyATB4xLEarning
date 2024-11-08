# Understanding of Global and Local variable.

public_toilet = "PT" #Global Variable

def family_members():
    print("Family members can use", public_toilet) # Family members can use public toilet
family_members()


def strangers():
    print("Strangers can use ", public_toilet) #Strangers can also use private toilet
strangers()


def home():
    private_toilet = "PvT"
    print("Only Family members can use ", private_toilet) #Only Home members will user private toilet.
home()