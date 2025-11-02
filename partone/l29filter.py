# filter()

# ? syntax
# ? filter(function,iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def iseven(num):
    return num % 2 == 0


result1 = filter(iseven, numbers)

print(result1)  # ? <filter object at 0x7f69e52982b0>
print(list(result1))  # ? [2, 4, 6, 8, 10]

result2 = filter(lambda x: x % 2 == 0, numbers)
print(result2)  # ? <filter object at 0x7f5283b9c580>
print(list(result2))  # ?  [2, 4, 6, 8, 10]


# todo filter more than 5 letters

backend = ["python", "php", "laravel", "nodejs"]

result3 = list(filter(lambda letter: len(letter) > 5, backend))

print(result3)  # ? ['python', 'laravel', 'nodejs']


# todo with tuple

tuples = (10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65)

result4 = tuple(filter(lambda x: x > 30, tuples))

print(result4)  # ? (35, 40, 45, 50, 55, 60, 65)


# todo with dictionary

students = {"susan": 12, "alice": 22, "bob": 15, "john doe": 55}

print(
    students.items()
)  # ? dict_items([('susan', 12), ('alice', 22), ('bob', 15), ('john doe', 55)])

result4 = dict(filter(lambda student: student[1] > 18, students.items()))

print(result4)  # ? {'alice': 22, 'john doe': 55}

# todo with set
numberset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

result5 = set(filter(lambda x: x % 2 == 0, numberset))

print(result5)  # ? {2, 4, 6, 8, 10}

# todo remove None and ""

datas = [True, 1, None, False, 2, None, "", 3, True, "", None]

result6 = list(filter(lambda x: x is not None and x != "", datas))

print(result6)  # ? [True, 1, False, 2, 3, True]
