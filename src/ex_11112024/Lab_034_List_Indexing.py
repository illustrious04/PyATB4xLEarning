# Indexing
from math import trunc

my_list = [1,2,3,4,5,6,7,8,9, "Suyash", True]

print(my_list)
print("Element at index 0 -> ", my_list[0])
print("Element at index 0 -> ", my_list[4])

# You can change the value also.
my_list[4] = "Suyash Guha"
print(my_list[4])

print("_______________________________________")
my_list.append(10)
print(my_list)


# extend will add the list inside the list.
print("--------------Extended list with extend function")
my_list.extend([11,12,13,14, "Hello Extended list"])
print("Extended list-> ",my_list)


# insert function will add the item in between the list.
print("------------------insert function--------------")
my_list.insert(2,"Second index changed")
print(my_list)

# Insert will insert the value before the origional value

# To replace any value just reassign the valur
my_list[4] = "5 is replaced with 500"
print(my_list)

my_list.insert(-1, "Ayush")