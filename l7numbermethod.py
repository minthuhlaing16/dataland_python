num1 = 123.45
print(int(num1))

num2 = "400"
print(int(num2))

# num3 = "300.12"
# print(int(num3)) # ValueError: invalid literal for int() with base 10: '300.12'

num4 = 100
print(abs(num4))  # 100

num5 = -100
print(abs(num5))  # 100

num6 = 2.6543
print(float(num6))  # 2.6543

num7 = 5
print(float(num7))  # 5.0

num8 = 4.5685
print(round(num8))  # 5
print(round(num8, 1))  # 4.6
print(round(num8, 2))  # 4.57
print(round(num8, 3))  # 4.569


print(pow(2, 3))  # 8

# 10 // 2 = 5,10 % 2 = 0
print(divmod(10, 2))  # (5, 0)
print(divmod(9, 2))  # (4, 1)
print(divmod(100, 3))  # (33, 1)

print(max(10, 20, 10, 2, 44, 20, 4, 5, 6))
print(min(1, 2, 3, 4, 5, 6, 7, 8))

print(sum([1, 2, 3, 4, 5]))  # 15 ==> list
print(sum((1, 2, 3, 4, 5)))  # 15 ==> tuple


# Mathematical Functions (from math module)
# To use the math module ! you need to import

import math

print(math.pow(2, 4))  # 16.0
print(math.pow(2, 2))  # 4.0

print(math.sqrt(32))  # 5.656854249492381
print(math.sqrt(64))  # 8.0

print(math.ceil(3.2))  # 4
print(math.ceil(3.6))  # 4

print(math.floor(3.2))  # 3
print(math.floor(3.6))  # 3


# e ==> (Euler number) is approximately
print(math.e)  # 2.718281828459045

print(math.log(100, 10))  # 2.0
print(math.log(81, 9))  # 2.0

print(math.log(10, 2))  # 3.3219280948873626
print(math.log(100, 2))  # 6.643856189774725

# default is e
print(math.log(100))  # 4.605170185988092

print(math.log10(100))  # 2.0
print(math.log10(1000))  # 3.0

print(math.log2(8))  # 3.0


# math.exp(exponential) , base is e
print(pow(2.718281828459045, 2))  # 7.3890560989306495
print(math.exp(2))  # 7.38905609893065

print(pow(2.718281828459045, 3))  # 20.085536923187664
print(math.exp(3))  # 20.085536923187668


import random

print(random.random())  # 0.3485550686265376
print(random.random())  # 0.925317160247256


# return a integer between x , y
print(random.randint(1, 10))  # ==> 1 to 10 kyr random


# return a float between x and y
print(random.uniform(1.5, 3.5))  # 1.5 ka nay 3.5 kyr float ko return pyan mal

numlists = [10, 20, 30, 40, 50]
print(random.choice(numlists))  # ==> pay htr tat 10 ka nay 50 hti bae return pyan mal

numtuples = 11, 22, 33, 44, 55
print(random.choice(numtuples))

numtuples = (66, 77, 88, 99, 100)
print(random.choice(numtuples))
