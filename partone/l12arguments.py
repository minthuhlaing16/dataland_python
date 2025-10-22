# Type of arguments in python
# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-length Arguments (*args) (non keyword variable arguments)
# Variable-length Arguments (**kwargs) (keyword variable arguments)


# Positional Arguments
def greet(name, age):
    print(f"Hello Friend,My name is {name},I am {age} years old.")


greet("susu", 23)  # Hello Friend,My name is susu,I am 23 years old.
greet(23, "nunu")  # Hello Friend,My name is 23,I am nunu years old.


# Keyword Arguments
def hifi(name, age):
    print(f"Hi {name}, I am {age} years old.")


hifi(name="John Doe", age=23)  # Hi John Doe, I am 23 years old.
hifi(age=25, name="Alice")  # Hi Alice, I am 25 years old.


# Default Arguments
def greeting(name="Hla Hla", age=33):
    print(f"My name is {name}, I am {age} years old. Nice to meet you.")


greeting()  # My name is Hla Hla, I am 33 years old. Nice to meet you.


# Variable-length Arguments (*args) (non keyword variable arguments)


def boys(*name):
    print(name)


boys("aung aung")  # ('aung aung',)
boys("aung aung", "kyaw kyaw", "moe moe")  # ('aung aung', 'kyaw kyaw', 'moe moe')
# boys("moe moe", name="aung kyaw") # error when including keyword arguments


def sumresults(*numbers):
    total = sum(numbers)
    print(f"Sum result is: {total}")


sumresults(30, 20, 10)  # Sum result is: 60
sumresults(23, 430, 23, 55, 64, 24)  # Sum result is: 619


def myfunone(num, *nums):
    print(num)  # 1
    print(nums)  # (3, 4, 5, 6, 7)


myfunone(1, 3, 4, 5, 6, 7)


def myfuntwo(name, *names):
    print(f"I have many friends. They are {names},but my fav friend is {name}.")


myfuntwo(
    "Su Su", "John Doe", "Alice", "bob", "maung maung"
)  # I have many friends. They are ('John Doe', 'Alice', 'bob', 'maung maung'),but my fav friend is Su Su.


# Variable-length Arguments (**kwargs) (keyword variable arguments)
def personinfos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")


personinfos(name="mya mya", age=22, city="Mandalay")
personinfos(name="Aung Aung", professional="Engineer", city="Yangon")
personinfos(name="Hla Hla", gender="Female")


# Exercise ==> combine different types of arguments
def emailsender(address, *messages, **files):
    print(f"Address - {address}")
    if messages:
        for message in messages:
            print(f"Message - {message}")
    if files:
        for key, value in files.items():
            print(f"{key} = {value}")


emailsender(
    "dataland@gmail.com",
    "WDF23332",
    "I want video record.",
    lessons="Python Batch 1",
    class_date="22/5/2025",
)

emailsender("test@gmail.com")


def studentinfos(name, age=20, *hobbies, **infos):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    if hobbies:
        print(f"I like {hobbies}.")
    if infos:
        for key, value in infos.items():
            print(f"{key} - {value}")


studentinfos("aung aung")
studentinfos(
    "aung aung",
    33,
    "gaming",
    "coding",
    "reading",
    profession="coding",
    carrier="web development",
)


def staffinfos(name, age=18, *hobbies, **infos):
    print(f"Name = {name}")
    print(f"Age: {age}")
    if hobbies:
        print(f"Hobbies : {" , ".join(hobbies)}")
    if infos:
        for key, value in infos.items():
            print(f"{key} - {value}")


staffinfos(
    "hla hla",
    33,
    "swimming",
    "eating",
    "playing",
    profession="coding",
    carrier="designer",
)
