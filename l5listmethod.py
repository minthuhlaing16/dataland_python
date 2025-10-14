names = ["aung aung", "maung maung", "su su", "yu yu"]
print(names)

mixeds = ["aung aung", 23, True, ["red", "green"], 22.22]
print(mixeds)
print(mixeds[1])
print(mixeds[3])
print(mixeds[3][0])
print(mixeds[3][1])

print(len(mixeds))  # 5
print(len(mixeds) - 1)  # 4
print(mixeds[len(mixeds) - 1])  # 22.22

print(mixeds[-1])  # 22.22
print(mixeds[-2])  # ['red', 'green']

print(mixeds[0:1])  # ['aung aung']
print(mixeds[0:2])  # ['aung aung', 23]
print(mixeds[1:3])  # [23, True]
print(mixeds[0:5])  # ['aung aung', 23, True, ['red', 'green'], 22.22]

# start:end:step
print(mixeds[0:5:2])  # ['aung aung', True, 22.22]

mix2 = mixeds[:]
mix2 = mixeds[0:3]
mix2 = mixeds[::-1]  # [22.22, ['red', 'green'], True, 23, 'aung aung']
print(mix2)


getlength = len(mix2)
print(getlength)

colors = ["red", "green", "blue"]
print(colors)  # ['red', 'green', 'blue']

colors[0] = "orange"
print(colors)

# colors[3] = "black" # IndexError: list assignment index out of range
# print(colors)

# append() array a nout ka value ta khu toe tar
colors.append("black")
print(colors)  # ['orange', 'green', 'blue', 'black']

# extend() multi value a nout ka toe tar; array nae pay ka mal
colors.extend(["gold", "silver"])
print(colors)  # ['orange', 'green', 'blue', 'black', 'gold', 'silver']

# insert(index,value)
colors.insert(0, "white")
print(colors)  # ['white', 'orange', 'green', 'blue', 'black', 'gold', 'silver']


# remove() ==> value and index
colors.remove("blue")
print(colors)  # ['white', 'orange', 'green', 'black', 'gold', 'silver']

# pop() ==> remove from end value and index
colors.pop()
print(colors)  # ['white', 'orange', 'green', 'black', 'gold']

# del ==> remove value and index
del colors[1]  # ['white', 'green', 'black', 'gold']
del colors[1:3]  # ['white', 'gold']
print(colors)


vals = [1, 2, 3, 4, 5]
print(f"Before clear values {vals}")  # Before clear values [1, 2, 3, 4, 5]
vals.clear()
print(f"After clear values {vals}")  # After clear values []


boys = [
    "aung aung",
    "maung maung",
    "kyaw kyaw",
    "ko oo",
    "hla myint",
    "zorrow",
    "the rock",
]

print(
    boys
)  # ['aung aung', 'maung maung', 'kyaw kyaw', 'ko oo', 'hla myint', 'zorrow', 'the rock']


# sort() a to z sin tar
boys.sort()
print(
    boys
)  # ['aung aung', 'hla myint', 'ko oo', 'kyaw kyaw', 'maung maung', 'the rock', 'zorrow']


# reverse()
boys.reverse()
print(
    boys
)  # ['zorrow', 'the rock', 'maung maung', 'kyaw kyaw', 'ko oo', 'hla myint', 'aung aung']


nums = [1, 22, 3, 44, 298, 22, 11, 4, 5, 3, 7]


nums.sort()
print(nums)  # [1, 3, 3, 4, 5, 7, 11, 22, 22, 44, 298]


nums.reverse()
print(nums)  # [298, 44, 22, 22, 11, 7, 5, 4, 3, 3, 1]


message = "Lorem john doe ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development. john doe Its purpose is to permit a page layout to be designed, independently of the copy that will subsequently populate john doe it, or to demonstrate various fonts of a typeface without meaningful text that could be distracting. Lorem ipsum is typically a corrupted version of De finibus john doe bonorum et malorum, a 1st-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin."

count_john_doe = message.count("john doe")
print(count_john_doe)  # 4

count_nums = nums.count(22)
print(count_nums)  # 2


# nested list
numbers = [1, 2, 4, [5, 6, 7, [8, 9, 10]]]
print(numbers)
print(numbers[3][3][2])

numbers.append([200, 300, 400])
print(numbers)  # [1, 2, 4, [5, 6, 7, [8, 9, 10]], [200, 300, 400]]

numbers.pop(1)
print(numbers)  # [1, 4, [5, 6, 7, [8, 9, 10]], [200, 300, 400]]


ages = [2, 11, 34, 56, 78, 22, 22, 11, 67, 11]

print(ages.count(11))  # 3

print(ages.index(11))  # 1 ==> value pay pee index shar tar


greeting = ["hello", "susu"]

print(greeting)  # ['hello', 'susu']
print(" ".join(greeting))  # hello susu
print(" - ".join(greeting))  # hello - susu


# list unpacking
val1, val2 = greeting

print(val1)
print(val2)

# list() , create a new list
greeting = "hello sir how are you?"
print(greeting)  # hello sir how are you?
print(
    list(greeting)
)  # ['h', 'e', 'l', 'l', 'o', ' ', 's', 'i', 'r', ' ', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']

# zip(,) looping pat loa ya tat kg mhan ta mya(lists,tuples,string)
arrone = ["10", "20", "30"]
arrtwo = ["hi", "hello", "hay"]
createzip = zip(arrone, arrtwo)
print(createzip)  # <zip object at 0x7fdf986a3480>

convert_to_list = list(createzip)
print(convert_to_list)  # [('10', 'hi'), ('20', 'hello'), ('30', 'hay')]
