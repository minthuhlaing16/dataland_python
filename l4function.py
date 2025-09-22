# ==> Function

# 1. Simple Function with no Parameter
# 2. Function with Parameter
#  (i) Single Parameter
#  (ii) Multi Parameter
# 3. Default parameter function
# 4. Function with a return value
# 5. Function with multi return value
# 6. Lambda Function (Anonymous Function)


# 1. Simple function with no Parameter
def sayname():
    print("My name is John Doe...")


sayname()

# 2. Function with Parameter (Single)


def saycity(city):
    print("Hello " + city)


saycity("Mandalay")


# 3. Default Parameter
def country(country="Myanmar"):
    print("Hello " + country)


country()
country("Singapore")


# 4. Single Return Function


def greeting(name):
    return "Hello my name is " + name + " how are you ?"


print(greeting("john doe"))

say_hi = greeting("Alice")

print(say_hi)


def saynickname(nickname="Daw Pu"):
    result = "My nickname is " + nickname + "."
    return result


print(saynickname())
print(saynickname("aung naing"))


def saynum(num1=0):
    return num1


print(saynum())
print(saynum(100))


def hihi(value):
    return f"Hello {value}"


print(hihi("Alice"))
print(hihi("bob"))


def funone(num1, num2=100):
    result = num1 + num2
    return f"Total value is {result}."


print(funone(10))
print(funone(20, 10))


# 5. Function with multi return value ==> return ...,...


def name_and_age():
    name = "Don Omar"
    age = 43
    city = "America"

    return name, age, city


print(name_and_age())

# Array destructure
[name1, age1, city1] = name_and_age()  # recommended
abc, efg, hij = name_and_age()

print(f"My name is {name1}, I am {age1} years old...")
print(abc, efg, hij)


# 6. Lambda Function (Anonymous Function)

hello = lambda name, age: f"hello {name},you are {age} years old"

print(hello("Bryan o corner", 33))

addresult = (
    lambda num1, num2: f"the sum of number one and number two is: {num1 + num2}..."
)

print(addresult(10, 20))

helloworld = lambda: "hello world! how are you? I am Bob..."
print(helloworld())


input_name = input("Enter your name: ")
print(f"Your name is {input_name}.. Right !!!")


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = f"Your full name is {last_name} {first_name} Right 😁 "
print(full_name)
