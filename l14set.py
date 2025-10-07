# Data Containers

# list
mylist = [1, 2, 3, 4, 5]
print(type(mylist))  # <class 'list'>

# tuple
mytuple = (1, 2, 3, 4, 5)
print(type(mytuple))  # <class 'tuple'>

# dic
mydic = {"a": 1, "b": 2, "c": 3}
print(type(mydic))  # <class 'dict'>

# set
myset = {1, 2, 3, 4, 5}
print(myset)  # {1, 2, 3, 4, 5}
print(type(myset))  # <class 'set'>

dic1 = {}
print(type(dic1))  # <class 'dict'>

set1 = {}
print(type(set1))  # <class 'dict'>

# create an empty set
set2 = set()
print(type(set2))  # <class 'set'>


colors = {"red", "green", "blue", "white", "black"}
print(colors)
print(type(colors))

for color in colors:
    print(color)

print("red" in colors)  # True
print("steelblue" in colors)  # False

fruits = {"apple", "orange"}
print(fruits)

# Adding a single Element
fruits.add("cherry")  # add ka single bae toe loa ya tal
print(fruits)  # {'apple', 'orange', 'cherry'}


# Adding a multi Elements []
fruits.update(["mango", "banana"])
print(fruits)  # {'apple', 'banana', 'orange', 'cherry', 'mango'}

# Remove Elements ==> element ma shi yin error pya tal ==> single remove
fruits.remove("apple")
print(fruits)  # {'orange', 'mango', 'cherry', 'banana'}

# Remove Element (Using discard())
fruits.discard("red")  # ma shi yin error ma pya buu , remove ka pya tal ma shi yin
fruits.discard("mango")
print(fruits)

# Remove all (clear)
fruits.clear()
print(fruits)  # set()

# Frozen set (Immutable of set)
fornumbers = frozenset([10, 20, 30])
print(fornumbers)  # frozenset({10, 20, 30})
print(type(fornumbers))  # <class 'frozenset'>
# fornumbers.add(50) # AttributeError: 'frozenset' object has no attribute 'add'
# fornumbers.remove(10) # AttributeError: 'frozenset' object has no attribute 'remove'
print(20 in fornumbers)  # True
print(50 in fornumbers)  # False


set3 = {1, 2, 3, 6, 7}
set4 = {3, 4, 6, 5}

# Union Combine (|) tuu tat har so override lote tal
print(set3 | set4)

# Intersection (&) tuu tat har bae yuu tar
print(set3 & set4)

# Difference (-)
print(set3 - set4)
print(set3.difference(set4))
print(set4 - set3)  # {4, 5}

# Symmetric Difference(^) ma tuu tar tway a kone yuu tar
print(set3 ^ set4)  # {1, 2, 4, 5, 7}
print(set4 ^ set3)  # {1, 2, 4, 5, 7}
print(set3.symmetric_difference(set4))  # {1, 2, 4, 5, 7}
print(set4.symmetric_difference(set3))  # {1, 2, 4, 5, 7}


# ==> set comprehension
# {expression for item in iterable condition}

squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}

evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}

uniquechars = {char for char in "Hello World"}
print(uniquechars)  # {'H', ' ', 'o', 'd', 'l', 'W', 'e', 'r'}

numbers = [1, 2, 2, 3, 4, 5, 7, 1, 2]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # {1, 2, 3, 4, 5, 7}

# ==> Nested Loops in set comprehension
couplenums = {(x, y) for x in range(3) for y in range(2)}
print(couplenums)  # {(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)}


""" print("hello world") """
