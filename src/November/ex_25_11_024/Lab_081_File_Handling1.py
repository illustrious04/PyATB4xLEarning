"""
# File Handling:
File Handling in Python:
	•	How to read a text file and and write into it with using Python code.
	•	Very important function: open(”file_name”, “mode”)
	•	Mode means how you want to open.
	•	‘r’ reading  mode (default)
	•	‘w’ writing mode
	•	‘a’ append
	•	‘b’ binary mode   zoom.exe (binary mode)
How to read and write
	•	Reading entire content : content = file_object.read()
	•	Reading for single line : line = file_object.readline()
	•	Reading All lines in a list: lines = file_object.readlines()
Close the file
"""


file = open('suyash.txt', 'r')
content = file.read()
print(content)







































