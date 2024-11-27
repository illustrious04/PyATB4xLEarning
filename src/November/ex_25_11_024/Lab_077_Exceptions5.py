"""
# Exceptions Handling:

# File Handaling
"""

try:
    file = open('exampl/txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'example/txt'
    print(file.read())
except Exception as fnfe:
    print("File Not found, fixed the path or create a file.")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
