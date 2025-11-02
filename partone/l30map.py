# map()

# ? syntax
# ? map(function,iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(num):
    return num**2


result1 = map(square, numbers)

print(result1)  # ? <map object at 0x7f6142a982e0>
print(list(result1))  # ? [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


result2 = map(lambda x: x**2, numbers)

print(list(result2))  # ? [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# todo difference between filter() and map()

result3 = list(filter(lambda x: x % 2 == 0, numbers))

print(result3)  # ? [2, 4, 6, 8, 10]

result4 = list(map(lambda x: x % 2 == 0, numbers))

print(result4)  # ? [False, True, False, True, False, True, False, True, False, True]

# todo converting string to upper , lower , capitalize

backend = ["python", "Nodejs", "PHP"]

result4 = list(map(str.upper, backend))

print(result4)  # ? ['PYTHON', 'NODEJS', 'PHP']

result5 = list(map(str.lower, backend))

print(result5)  # ? ['python', 'nodejs', 'php']

result6 = list(map(str.capitalize, backend))

print(result6)  # ? ['Python', 'Nodejs', 'Php']


# ! casefold and lower are the same
result7 = list(map(str.casefold, backend))

print(result7)  # ? ['python', 'nodejs', 'php']


# todo nested list

nestedlist = [[10, 20], [30, 40], [50, 60]]
result8 = list(map(lambda x: x[0] + x[1], nestedlist))

print(result8)  # ? [30, 70, 110]

# todo with a tuple

tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

result9 = tuple(map(lambda x: x / 10, tuples))

print(result9)  # ? (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)


# todo with Dictionary
students = {"susu": 10, "nunu": 23, "pupu": 30, "yuyu": 12}
# print(students.items())

result10 = dict(map(lambda student: (student[0], student[1] * 2), students.items()))

print(result10)  # ? {'susu': 20, 'nunu': 46, 'pupu': 60, 'yuyu': 24}


# todo with set

numberset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

result11 = set(map(lambda x: x * 2, numberset))

print(result11)  # ? {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# todo multi iterables
# ? [1+5,2+6,...]

num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

result12 = list(map(lambda x, y: x + y, num1, num2))

print(result12)  # ? [6, 8, 10, 12]
