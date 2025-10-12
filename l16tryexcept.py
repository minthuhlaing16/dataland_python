# ==> Exception Handling

# try:
# exception
# except exceptiontype:
# code to handle the exception

# ==> exceptiontype
# (i) ValueError
# (ii) ZeroDivisionError

# try:
#     lucky_number = int(input("Enter your lucky number: "))
#     print(f"Your lucky Number is ==> {lucky_number}")
# except:
#     print("Something went wrong... Try Again and enter a valid number...")

# ==> Specific Exception

# try:
#     number = int(input("Enter number: "))
#     print(10 / number)
# except ValueError:
#     print("Invalid input! Please eneter a valid number...")
# except ZeroDivisionError:
#     print("You can't divided by zero...")

# else and finally
# else Block (Optional) = execute only if no exception occurs in the try block
# finally Block (Optional) = execute whether or not an exception occurs

# try:
#     number = int(input("Enter a random number: "))
#     result = 10 / number
# except ValueError:
#     print("Invalid input! Please enter a valid number...")
# except ZeroDivisionError:
#     print("You can't divided by zero...")
# else:
#     print(f"Your number divided by 10 is : {result}")
# finally:
#     print("The program is complete..")


# Raising Exception
try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise ValueError("Age can't be zero or less than zero. Try again..")
    else:
        print(f"You are {age} years old...")
except ValueError as err:
    print(f"Error: {err}")
