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

numitems["val"] = 1
print(numitems)  # defaultdict(<class 'int'>, {'val': 1})

numitems["val"] += 2
print(numitems)  # defaultdict(<class 'int'>, {'val': 3})

print(numitems["val"])  # 3
