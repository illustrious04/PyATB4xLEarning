# Tuple

"""
It is also a collection item
my_tuple = (1,3,5,6)
but you can not change the value.
They are immutable in nature, value can not be reassign
Duplicate is also allowed in Tuple

When we have to use Tuple:
"""

# my_tuple = ("abc.com", "wer.com")

# tuple_new = (1,2,3,4,5,)
# tuple_new[3] = 64 # Immutable in nature.
# print(tuple_new)  # TypeError: 'tuple' object does not support item assignment

# When we have to use tuple:

# Real world project

domain = ("tta.com", "sdet.club") # Domains will not change in this case we will use tuple.
print("This is Tuple ", domain)
# We can convert tuple to list

my_api_list = list(domain)
print("Tuple converted to list",my_api_list)
