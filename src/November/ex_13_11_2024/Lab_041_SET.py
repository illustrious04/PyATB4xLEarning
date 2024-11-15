# SET => Is a collection of unique elements
# Used to remove the duplicates.

list_of_unique_elements = {1,2,3,4,4,5,5,8,9}
print(list_of_unique_elements)

print("-----------------------------------------------------")
# If want to remove any element from the list use SET
list = [22.45, 22.45, 34,56,77.77,88]
set1 = set(list)
print(set1)

print("-------------------------SET with Union----------------------------")
# SET is also supported with Union
uni_set1 = {1,2,3,4}
uni_set2 = {5,6,7,8}
my_set = uni_set1.union(uni_set2)
print(my_set)

print("-------------------------SET with Intersection----------------------------")
uni_set3 = {1,2,3,4,5}
uni_set4 = {4,5,6,7,8}
my_set_1 = uni_set3.intersection(uni_set4)
print(my_set_1)

print("-------------------------SET with Difference----------------------------")
uni_set5 = {1,2,3,4,5}
uni_set6 = {4,5,6,7,8}
# my_set_2 = uni_set5.difference(uni_set6)
my_set_2 = uni_set6.difference(uni_set5)
print(my_set_2)