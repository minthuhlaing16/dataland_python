# ==> dictionary Comprehension
# {key:valueexpression for item in iterable}

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

evens = {x: x for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

# create dictionary from two lists
keys = ["fullname", "age", "city", "country"]
values = ["Yamone oo", 25, "Mandalay", "Myanmar"]

result_dict = {keys[x]: values[x] for x in range(len(keys))}
print(
    result_dict
)  # {'fullname': 'Yamone oo', 'age': 25, 'city': 'Mandalay', 'country': 'Myanmar'}


combinedict = {key: val for key, val in zip(keys, values)}
print(
    combinedict
)  # {'fullname': 'Yamone oo', 'age': 25, 'city': 'Mandalay', 'country': 'Myanmar'}


# modifying values in a dictionary

# original dictionary
original_dictionary = {"x": 1, "y": 2, "z": 3}
print(
    f"original dic: {original_dictionary}"
)  # old dictionary: {'x': 1, 'y': 2, 'z': 3}

new_dictionary = {key: val * 2 for key, val in original_dictionary.items()}
print(f"new dictionary: {new_dictionary}")  # new dictionary: {'x': 2, 'y': 4, 'z': 6}

# create dictionary from a string
sayhi = "Hello World"
count_chars = {char: sayhi.count(char) for char in set(sayhi)}
print(count_chars)  # {' ': 1, 'e': 1, 'o': 2, 'l': 3, 'r': 1, 'd': 1, 'W': 1, 'H': 1}
