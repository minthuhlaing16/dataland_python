# ==> Write a File

# Note: linux mar permission pay ka mal yay loa ma ya yin ==> sudo chomd 777 -R files/

# mode
# 'r' = Read (Default)
# 'w' = Write
# 'a' = Append

# syntax
# open('filename.txt',mode)

# ==> Write File
# write()
# writelines()

# Method 1 , write()
print("\n Method 1, write()")

file = open("files/file2.txt", "w")
file.write("hello world how are you ?!")
file.close()  # Always need to close to save changes

# Method 2 , writelines()
print("\nwritelines()")
lines = [
    "Hello John Doe! \n",
    "How are you? \n",
    "My name is Alice \n",
    "Nice to meet you. \n",
]
file = open("files/file3.txt", "w")
file.writelines(lines)
file.close()

# Using with statement
print("\nusing with statement.")
with open("files/file4.txt", "w") as file:
    file.write("What are you doing? John. \n")
    file.write("You suppose to go to work. \n")
    file.write("lazy ass motherfucker... \n")

# ==> Append to a file
print("\nAppend to a file")

with open("files/file5.txt", "a") as file:
    file.write("\n hello MotherFucker! \n")

# using variable
print("\n using variables")
name = "Aung Kyaw"
age = 23

with open("files/file6.txt", "w") as file:
    file.write(f"My name is {name}, I am {age} years old...")

# Error Handling
print("\n Error Handling")
try:
    with open("files/file7.txt", "w") as file:
        file.write(
            f"hello world My name is {name} and I am {age} years old mother fucker. \n"
        )
except Exception as err:
    print(f"IO Error : {err}")  #! IOError/Exception ==> General case
finally:
    print("Program Completed! Mother Fucker...")
