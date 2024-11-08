# * arguments.
#*args = Multiple arguments with No limit--> list
def print_arguments(*args):
    print(args[0])
    for i in args:
        print(i)

print_arguments("Suyash", "Amit", "Ashwin")
print_arguments("Amit", 10)
print_arguments("Amit", 10, True, False)
print_arguments("Amit", 10, True, False, "SUYASH")


