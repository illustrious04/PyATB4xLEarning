#Escape sequence

print("Hello World")
print("Hello\nworld") #\n-> New Line
print("Hello\tworld") #\t-> Tab line
print("Hello\bWorld") #\-> Backspace

# dir = 'c:\suyash\n.txt' #This will give an Escape sequence error
# To fix this we can put it inside double quates
# dir = "c:\suyash\n.txt" #But now this will consider as new line \n.txt

# To fix this, we need to use r which means raw

dir1 = r"c:\suyash\n.txt" # Output will be c:\suyash\n.txts
#This r concept will be used in API automation, when we use file path we will use r concept
# r will also works with single quate

dir2 = r'c:\suyash\n.txt"'
print(dir1)
print(dir2)
