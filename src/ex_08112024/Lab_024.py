# Play with functions. and list

my_shopping_list = ["Bread", "Butter", "Eggs"]
print(my_shopping_list)
print(len(my_shopping_list))

def bring_more_item(my_new_list):
    my_new_list.append("Cheese")
    return my_new_list

l = bring_more_item(my_shopping_list)
print(l)


#Taking user input:
def bring_more_item_new(my_new_list):
    more_item = input("Enter the item\n")
    my_new_list.append(more_item)
    return my_new_list
new_list = bring_more_item_new(my_shopping_list)
print(new_list)

































