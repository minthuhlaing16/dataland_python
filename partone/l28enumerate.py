# enumerate()

colors = ["red", "green", "blue"]

for color in colors:
    print(color)

for index, color in enumerate(colors):
    print(index, color)

numbers = [10, 20, 30, 40, 50]

for idx, value in enumerate(numbers):
    numbers[idx] = value * 2
    # print(numbers[idx])

print(numbers)  # ? [20, 40, 60, 80, 100]


colors = ["red", "green", "blue", "white", "black"]

for idx, color in enumerate(colors):
    if color == "black":
        print(f"Black color exit.")  # ? Black color exit. ==> case sensative

# todo custom start idx

names = ["john doe", "susan", "bob", "alice", "hla hla"]

# ? index 10 ka sa mar
for idx, name in enumerate(names, 10):
    print(f"Index {idx} : {name}")


# todo string ko san mal

message = "Hello World!"

for idx, msg in enumerate(message):
    print(idx, msg)

colors = ["Red", "Green", "Blue", "Black", "White"]

colorlist = list(enumerate(colors, 100))

print(
    colorlist
)  # ? [(100, 'Red'), (101, 'Green'), (102, 'Blue'), (103, 'Black'), (104, 'White')]
