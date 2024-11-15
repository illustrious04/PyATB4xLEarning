set1 = {1,2,3,4,5}
set2 = {2,3,8}
subset = set2.issubset(set1)
print(subset) # This will give bool value.

print("-------------------------------------------")
set3 = set(["Testing", "for" , "Testing."])
print("Length of set 3 is -> ",len(set3))

for i in set3:
    print(i)

set3.add("Suyash")
print(set3)