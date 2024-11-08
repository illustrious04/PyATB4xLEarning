"""
A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward,
ignoring spaces, punctuation, and capitalization.
In other words, if you reverse the order of the characters, it still reads the same.
Examples:
    "madam", "racecar" "level"
    "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?"
    121 12321 98789
"""

# Approach-1
"""
#Take User Input
text = input("Enter a word to check if it is a palindrome: ")
# Convert text to lowercase to make the check case-insensitive
text = text.lower()
# Check if the string is a palindrome using a loop
is_palindrome = True
for i in range(len(text)//2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
"""

""" Approach-2 
By Using Using the reversed() Function
1) Use reversed(): This creates a reversed iterator of the string.
2) Join the reversed iterator: ''.join(reversed(text)) converts the reversed iterator back into a string.
"""

text = input("Enter a word to check if it is a palindrome: \n")

if text.lower() == ''.join(reversed(text.lower())):
    print(f"{text} is a palindrome. ")
else:
    print(f"{text} is not a palindrome. ")




