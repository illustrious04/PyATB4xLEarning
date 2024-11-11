# Playing with list
print("This is My list with 5 elements")
my_list = [1,2,3,4,5]
print(my_list)
print("--------------------------------")

print("Adding -1")
my_list.insert(-1, 6)
print(my_list) # Output: 6 will be placed before 5.
print("Updated Length of the list -> ",len(my_list))

print("----------------Remove an element-------------------")
my_list.remove(4)
print(my_list)

# We can also create a copy of the list
print("-------------------------------------------------")
my_copy_list = my_list.copy()

print("List is copied",my_copy_list)
print("List is copied",my_list)

print("---------Sorting of the list")
my_new_list = [0,5,8,6,4,7,8]
print("Original list", my_new_list)
my_new_list.sort()
print("Sorted list", my_new_list)

print("-----Reverse of the list")
my_new_list.reverse()
print("Revere list", my_new_list)
