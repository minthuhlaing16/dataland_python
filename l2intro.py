# print("hello Python")


# ==> Arithmetic Operator
# + Addition
# - Subtraction
# * Multiplication

# / Division (float division)
# % Modulus
# // Floor Division

# ** Exponent


print(20 + 5)
print(20 - 5)
print(20 * 5)
print(20 / 5)
print(20 // 5)
print(20 % 5)
print(2**2)
print(2**3)


# ==> Operator Precedence(PEMDAS)
# Parentheses
# Exponent
# Multiplication Division (firstin/firstcal)
# Addition Subtraction  (fistin/fastcal)


print(2 + 5 * 4 / 10 - 10 % 2)  # 4.0


first_name = "Aung Kyaw"
last_name = "Kyaw Aung"

print(first_name)
print(last_name)
print(first_name, last_name)

x = 10
y = 30
p = "20"
q = "30"

sum1 = x + y
sum2 = p + q

print(sum1)
print(sum2)

# print(x + q) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

num1 = 100
num2 = 100.125
name = "Su Su"

print(num1, num2)


# Data sit mal so yin type()

print(type("hello"))  # <class 'str'>
print(type(124))  # <class 'int'>
print(type(True))  # <class 'bool'>
print(type(12.3))  # <class 'float'>


colors = ["red", "green", "blue"]

print(colors)
print(type(colors))  # <class 'list'>

ages = [12, 44, 40]
print(ages)
