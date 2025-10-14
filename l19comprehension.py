# ==> List Comprehension
# [expression for item in iterable]

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# list comprehension with String
chars = [char for char in "Hello World"]
print(chars)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']


numbers = [1, 2, 2, 3, 4, 5, 7, 1, 2]
numbers_ = [x for x in numbers]
print(numbers_)  # [1, 2, 2, 3, 4, 5, 7, 1, 2]

# ==> Nested Loops in list comprehension
couplenums = [(x, y) for x in range(3) for y in range(2)]
print(couplenums)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# ==> Nested list comprehension

nestnumberarr = [[1, 2, 3], [40, 50, 60], [700, 800, 900]]
flatarrs = [y for x in nestnumberarr for y in x]
print(flatarrs)  # [1, 2, 3, 40, 50, 60, 700, 800, 900]

# for x in nestnumberarr
# first iteration x = [1,2,3]
# second iteration x = [40,50,60]
# third iteration x = [700,800,900]

# for y in x
# first iteration x = [1,2,3] . process y = 1, y = 2, y = 3
# second iteration x = [1,2,3] . process y = 40 , y = 50 , y = 60
# third iteration x = [1,2,3] . process y = 700 , y = 800 , y = 900
