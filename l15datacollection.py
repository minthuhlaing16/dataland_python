# ==> Data Collection (Module Containers)

from collections import Counter

# ==> counter (from collections module)
getcounts = Counter("Hello World")
print(
    getcounts
)  # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})


# ==> deque (from collections module)
from collections import deque

qpersons = deque(["Su Su", "Nu Nu", "Yu Yu"])
print(qpersons)  # deque(['Su Su', 'Nu Nu', 'Yu Yu'])

qpersons.append("Hla Win")
print(qpersons)  # deque(['Su Su', 'Nu Nu', 'Yu Yu', 'Hla Win'])

qpersons.appendleft("Aung Kyaw")
print(qpersons)  # deque(['Aung Kyaw', 'Su Su', 'Nu Nu', 'Yu Yu', 'Hla Win'])

for qperson in qpersons:
    print(qperson)

# remove from right
qpersons.popleft()
print(qpersons)  # deque(['Su Su', 'Nu Nu', 'Yu Yu', 'Hla Win'])

qpersons.pop()
print(qpersons)  # deque(['Su Su', 'Nu Nu', 'Yu Yu'])


# ==> defaultdict (from collections module)

from collections import defaultdict

items = defaultdict(list)

items["fruits"].append("apple")
items["fruits"].append("banana")
items["fruits"].append("pineapple")
items["fruits"].append("mango")
items["fruits"].append("orange")
items["colors"].append("red")
items["colors"].append("blue")
items["colors"].append("green")
items["colors"].append("black")

print(items["colors"])  # ['red', 'blue', 'green', 'black']
print(items["fruits"])  # ['apple', 'banana', 'pineapple', 'mango', 'orange']
print(items["candy"])  # []

numitems = defaultdict(int)

print(numitems)  # defaultdict(<class 'int'>, {})

print(numitems["val"])  # 0

numitems["val"] = 1
print(numitems)  # defaultdict(<class 'int'>, {'val': 1})

numitems["val"] += 2
print(numitems)  # defaultdict(<class 'int'>, {'val': 3})

print(numitems["val"])  # 3

# Grouping Items
groups = defaultdict(list)
foods = [
    ("fruits", "apple"),
    ("fruits", "mango"),
    ("fruits", "orange"),
    ("colors", "red"),
    ("colors", "blue"),
    ("colors", "green"),
    ("vegetables", "carrot"),
    ("vegetables", "raddish"),
]

for key, value in foods:
    groups[key].append(value)
print(
    groups
)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'mango', 'orange'], 'colors': ['red', 'blue', 'green'], 'vegetables': ['carrot', 'raddish']})


# Counting Elements
colorcounts = defaultdict(int)
candycolors = ["red", "green", "blue", "black", "white", "red", "red", "green", "blue"]

for candycolor in candycolors:
    colorcounts[candycolor] += 1

print(
    colorcounts
)  # defaultdict(<class 'int'>, {'red': 3, 'green': 2, 'blue': 2, 'black': 1, 'white': 1})

# OrderedDict (from collection module)

from collections import OrderedDict

myorders = OrderedDict()
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(
    myorders
)  # OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})

print(myorders["num2"])  # 200

# Reordering Item
myorders.move_to_end("num2")
print(
    myorders
)  # OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# re-inserting
myorders["num1"] = 10
print(
    myorders
)  # OrderedDict({'num1': 10, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# delete
del myorders["num3"]
print(myorders)  # OrderedDict({'num1': 10, 'num4': 400, 'num5': 500, 'num2': 200})


config = OrderedDict()
config["host"] = "localhost"
config["port"] = 5000
config["debug"] = True

for key, value in config.items():
    print(f"{key} : {value}")

# nametuple (from collections module)
from collections import namedtuple

lucky_numbers = namedtuple("lucky_numbers", ["num1", "num2", "num3"])

getnums = lucky_numbers(33, 66, 99)

print(getnums.num1)  # 33
print(getnums.num2)  # 66
print(getnums.num3)  # 99

# exercise with tuple, hard to remember what index number represents
staff = ("Yu Yu", 20, "Developer")

print(staff[0])  # Yu Yu
print(staff[1])  # 20
print(staff[2])  # Developer

# namedtuple
student = namedtuple("student", ["name", "age", "profession"])
# Method 1
# pupil = student("susu", 23, "Developer")
# Method 2
pupil = student(name="susu", age=34, profession="engineer")
print(pupil.name)  # susu
print(pupil.age)  # 34
print(pupil.profession)  # engineer

# ChainMap from collection module

from collections import ChainMap

dic1 = {"name": "aung kyaw"}
dic2 = {"city": "Mandalay"}

getdata = ChainMap(dic1, dic2)
print(getdata)  # ChainMap({'name': 'aung kyaw'}, {'city': 'Mandalay'})

print(getdata["name"])  # aung kyaw
print(getdata["city"])  # Mandalay
