name = "Aung Kyaw"

print(name[0])  # A
print(name[1])  # u
print(name[2])  # n
print("________________________")

# reverse
print(name[-1])  # w
print(name[-2])  # a
print(name[-3])  # y
print("___________________________")

# start:end:step
print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[0:4])
print(name[1:4])
print(name[1:7])
print(name[0:9])
print(name[0:])

print(name[0:9:1])
print(name[0:9:2])

full_name = name
first_name = name[0:4]
last_name = name[5:9]
print(full_name)
print(first_name)
print(last_name)
print(full_name[:])
print(full_name[::-1])  # reverse

# array yae length ko ti chin yin len()
getlength = len(full_name)
print(getlength)

text = "how are you ? i am fine. thank you."

# uppercase ==> upper()
uppercase_text = text.upper()
print(uppercase_text)

# lowercase ==> lower() , casefold()
lowercase_text = uppercase_text.lower()
case_fold_text = uppercase_text.casefold()
print(lowercase_text)
print(case_fold_text)

# capitalize ==> capitalize()
capitalize_text = text.capitalize()
print(capitalize_text)


# sar lone a sa twae a kone lone kyii chin tal so ==> title()
title_text = text.title()
print(title_text)

todo = "Have To Shop"
swap_case = todo.swapcase()
print(swap_case)


# strip po nay tat space twae ko del tr
hifi = "        hello space         "
print(hifi)
print(hifi.strip())
print(hifi.lstrip())
print(hifi.rstrip())


# replace(old,new)
greet = "hello friend! How are you ?"
print(greet.replace("friend", "John"))
print(greet.replace("friend! How are you", "Bob. Are you ok"))

# startswith() return boolean
print(greet.startswith("h"))
print(greet.startswith("he"))
print(greet.startswith("He"))

# endswith() return boolean
print(greet.endswith("?"))
print(greet.endswith("you ?"))

mobile = "OPPO"
# isupper()
print(mobile.isupper())  # True
# islower()
print(mobile.islower())  # False
# istitle()
print(mobile.istitle())  # False


num1 = 123
num2 = "123"
num3 = "ten"

# isdigit() ==> String bae sit loa ya tal
# print(num1.isdigit)
print(num2.isdigit())  # True
print(num3.isdigit())  # False

# isalpha()
print(str(num1).isalpha())  # False
print(num2.isalpha())  # False
print(num3.isalpha())  # True

# isnumeric()
print(num2.isnumeric())  # True
print(num3.isnumeric())  # False

# isalnum()
print(num2.isalnum())  # True
print(num3.isalnum())  # True


# isspace() ==> sar lone ma par bae space gyii bae lar sit tar
middle_name = " "
print(middle_name.isspace())  # True

nickname = "Aung Aung"
print(nickname.isspace())  # False
print(nickname.istitle())  # True

# split()
sayhi = "Hi my friend"
print(sayhi.split())  # ['Hi', 'my', 'friend']

# rsplit()
colors = "red,green,blue,white,yellow"
print(colors.rsplit())  # ['red,green,blue,white,yellow']


# splitlines() ==> \n (newline nae sin htr mha array ta khan lote pay mar)
sayHello = "Hello \n My \n Friend"
print(sayHello.splitlines())  # ['Hello ', ' My ', ' Friend']

# partition()
sayhifi = "hello friend Mr. Maung"
print(sayhifi.partition(" "))  # ('hello', ' ', 'friend Mr Maung')
print(sayhifi.partition("."))  # ('hello friend Mr', '.', ' Maung')

post = "read"
print(post.ljust(10, "_"))  # read______
print(post.rjust(10, "_"))  # ______read
print(post.center(10, "_"))  # ___read___

post1 = "write"
print(post1.center(20, "-"))

num4 = "number ten"
num5 = "Hay!"
print(num4.isalnum())  # False  ==> space kyaung
print(num5.isalnum())  # special escape character par nay loa


city = "Hello {}"
print(city.format("Mandalay"))  # Hello Mandalay

country = "hello {} hi {}"
print(
    country.format("Mandalay", "Myanmar")
)  # hello Mandalay hi Myanmar ==> {} 2 khu so format(1,2)

# dictionary

user = {"name": "aung aung", "age": 32, "isMale": True}
greet = "Hello {name} , you are {age} years old."
print(greet.format_map(user))
