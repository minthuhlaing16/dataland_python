# List Vs Tuple
# 1.Mutability , mutable (change) and immutable (not change/fixed)

# 2.Performance
# list ==> Generally slower than tuple
# tuple ==> Generally faster than list and more efficient because they are immutable and have a fixed size

# 3. Use Cases
# list ==> need to change for example user lists ,shopping carts, etc...
# tuple ==> geographic coordinates,settings ,database records

# 4. Methods
#  lists ==> many build in methods for modifying list for example append(),remove(),pop(),sort().
#  tuple ==> fewer build in methods . cannot be modified. only can use .count(),.index()


print(type([1, 2, 3, 4]))  #  <class 'list'>
print(type((1, 2, 3, 4)))  # <class 'tuple'>

# Create a tuple with parantheses
tuple1 = (1, 2, 3, 4, 5, 5)
print(tuple1)  # [1, 2, 3, 4]

print(tuple1[0])  # 1
print(tuple1[2])  # 3
print(tuple1[3])  # 4

# Create tuple with no parentheses
tuple2 = 10, 20, 30, 40, 40
print(tuple2)  # (10, 20, 30, 40)

print(tuple2[0])  # 10
print(tuple2[2])  # 30
print(tuple2[3])  # 40

# tuple1[0] = 100  # TypeError: 'tuple' object does not support item assignment


print(tuple1.count(2))  # 1
print(tuple2.count(40))  # 2

print(tuple1.index(2))  # 1
print(tuple1.index(5))  # 4

# Tuple Unpacking

names = ("john doe", "Susan", "bob", "Alice")

boy1, girl1, boy2, girl2 = names

print(boy1)
print(boy2)
print(girl1)
print(girl2)

# Nested tuple
numbers = (1, 2, (3, 4, 5), (6, 7))  # (1, 2, (3, 4, 5), (6, 7))
print(numbers)
print("the value of index [2][1] is: ", numbers[2][1])
print("the value of index [3][1] is: ", numbers[3][1])
