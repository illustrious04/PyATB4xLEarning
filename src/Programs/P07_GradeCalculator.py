"""
Grade Calculator:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

Logic Building
1st ->
"""

score = int(input("Enter your score\n"))

if score >= 90 and score <= 100: # if 90 <= score <= 100: this also we can write in Python
    print("Your Grade is -", "A")
elif score >= 80 and score <= 89:
    print("Your Grade is -", "B")
elif score >= 70 and score <= 79:
    print("Your Grade is ", "C")
elif score >= 60 and score <= 69:
    print("Your grande is ", "D")
else:
    print("You got fail", "F")

