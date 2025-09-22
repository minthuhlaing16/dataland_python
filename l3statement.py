# ==> Comparison Operator

# == Equal
# != Not Equal
# > Greater Than
# < Less Than
# >= Greater Than or Equal
# <= Less Than or Equal

# is, is not (Identity Operators)
# in, not in (Membership Operators) ==> case sensitive

# if True:
#     print("Good Day")
# else:
#     print("Bad Day")


x = 10

if x == 11:
    print("X is equal to 10")
else:
    print("X is not equal to 10")


name = "Bob"

if name == "john doe":
    print("you are john doe. Welcome Sir !!!")
elif name == "Alice":
    print("you are Alice.")
else:
    print("Wrong User!!!")


if 5 >= 3:
    print("yes")
else:
    print("no")


names = ["aung aung", "maung maung", "zaw zaw"]

# = is assignment operator
students = names
teachers = ["john doe", "alice", "bob"]

print(names is students)  # True ==> boolean nae pyan pay mal
print(students is teachers)  # False
print(students is not teachers)  # True
print(students is not names)  # False

print("aung aung" in names)  # True
print("maung maung" in students)  # True
print("aung aung" in teachers)  # False
print("aung aung" not in teachers)  # True
print("john doe" not in teachers)  # False


# ==> isinstance(value,type)
print(isinstance("String", str))  # True
print(isinstance(23, int))  # True
print(isinstance(True, str))  # False


# isinstance() is not working on bool it only describe int because bool value is 0 or 1 that's why
is_array = ["string", 233, True]
user = {"name": "John Doe", "age": 33, "is_programmer": True}

test_datatype = user
if isinstance(test_datatype, str):
    print("This is String Datatype.")
elif isinstance(test_datatype, int):
    print("This is number Datatype.")
elif isinstance(test_datatype, bool):
    print("This is boolean DataType.")
elif isinstance(test_datatype, float):
    print("This is float DataType.")
elif isinstance(test_datatype, list):
    print("This is array/list DataType.")
elif isinstance(test_datatype, dict):
    print("This is dictionary/object DataType")
else:
    print("Enter something.")


# if isinstance(True, bool):
#     print("this is bool")  # this is bool
# else:
#     print("this is not bool")


person = {"name": "aung aung", "age": 23, "gender": "Male", "is_student": True}

print(person)
print(type(person))  # <class 'dict'>
