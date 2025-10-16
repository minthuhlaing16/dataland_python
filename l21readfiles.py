# ==> Open File
# mode
# 'r' = Read (Default)
# 'w' = Write
# 'a' = Append

# syntax
# open('filename.txt',mode)

# ==> Read File
# read() = Read the entire fle.
# readline() = Read on line at a time
# readlines() = Read all lines into a list.

# ==> Method 1, read() (with statement), Read all content at once, Not memory-efficient for large files . with statement ka file pate tar par pee tar twr pate sa yar ma lol
print("\nread()")
with open("./files/file1.txt", "r") as file:
    # print(file) # <_io.TextIOWrapper name='./files/file1.txt' mode='r' encoding='UTF-8'>
    getcontent = file.read()
    print(getcontent)

# ==> File Encoding
print("\nFile Encoding")
with open("files/file1.txt", "r", encoding="UTF-8") as file:
    getcontent = file.read()
    print(getcontent)

# ==> Read Specific Number of Characters
print("\nRead Specific Number of Characters")
with open("files/file1.txt", "r", encoding="UTF-8") as file:
    getcontent = file.read(11)  # Read the first 11 characters.
    print(getcontent)

# ==> Method 2, using strip(), Read line by line,(One line at a time. Efficient for large file)
print("\nusing strip()")
with open("files/file1.txt", "r") as file:
    for line in file:
        # print(line)
        print(line.strip())  # .strip() removes extra newline characters

# ==> Method 3, using readline(), Read line by line(one line at a time. Efficient for large file)
print("\nusing readline()")
with open("files/file1.txt", "r") as file:
    line = file.readline()
    # print(line)  # Hello World!
    while line:
        print(line.strip())
        line = file.readline()

# Method 4, using readlines(), Read all lines (all lines at once can use a lote of memory for large files)
print("\nusing readlines()")

with open("files/file1.txt", "r") as file:
    getcontent = file.readlines()
    # print(
    #     getcontent
    # )  # ['Hello World!\n', 'This is Python Batch 1 zoom class.\n', 'How to read file in python programming language.\n']
    for line in getcontent:
        # print(line)
        print(line.strip())

# ==> Handling Exception
# ==> exceptiontype
# (i) FileNotFoundError
# (ii) PermissionError
# (iii) IOError

print("\nHandling Exceptions")
try:
    with open("files/file1.txt", "r") as file:
        getcontent = file.read()
        print(getcontent.strip())
except FileNotFoundError:
    print("Your files does not exist..")
except PermissionError:
    print("You do not have the necessary permissions..")
except IOError as err:
    print(f"An IO error: {err}")
finally:
    print("Program Completed")
