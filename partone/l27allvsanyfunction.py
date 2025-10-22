# ==> all(iterable)
# ? Note (true): Non-zero numbers, non-empty,True
# ? Note (false): 0, empty,False

# todo List

boollists = [True, True, True]
print(all(boollists))  # * True

boollists = [True, False, True]
print(all(boollists))  # ! False

numlists = [1, 2, 3, 4, 5]
print(all(numlists))  # * True

numlists = [0, 1, 2, 3, 4, 5]
print(all(numlists))  # ! False

emptylists = []
print(all(emptylists))  # ? True

# todo ==> Tuple
booltuple = (True, True, True)
print(all(booltuple))  # * True

# todo ==> Set

numset = {1, 2, 3, 4, 5, 0}
print(all(numset))  # ! False

# todo Dictionary

colordict = {1: "red", 2: "green", 3: "blue"}
print(all(colordict))  # * True


colordict = {1: "red", 0: "green", 3: "blue"}
print(all(colordict))  # ! False

# ? Using Case

stringlists = ["red", "green", "blue"]
print(all(stringlists))  # * True

stringlists = ["red", "", "blue"]
print(all(stringlists))  # ! False

# ? Check all numbers are positive
numlists = [10, -20, 30, 40, 50]

checkpositive = all(num > 0 for num in numlists)
print(checkpositive)  # * True numlists mar - ma par yin true
print(checkpositive)  # ! False numlists mar - par yin false


print(
    "______________________________________________________________________________________________________________________________________________________"
)

# ? Note ==> any(iterable) ==> at least one element is truthy.

boollists = [True, True, True]
print(any(boollists))  # * True

boollists = [True, False, True]
print(any(boollists))  # * True

numlists = [1, 2, 3, 4, 5]
print(any(numlists))  # * True

numlists = [1, 2, 3, 0, 4]
print(any(numlists))  # * True

numlists = [0, 0, 0]
print(any(numlists))  # ! False

numlists = [0, 0, 0, 1]
print(any(numlists))  # * True

emptylists = []
print(any(emptylists))  # ! False

# todo Tuple
booltuple = (False, False, True)
print(any(booltuple))  # * True

# todo set
numset = {0, 0, 0, 2}
print(any(numset))  # * True

# todo dict
colordict = {1: "red", 2: "blue", 0: "white"}
print(any(colordict))  # * True

# todo using Case
stringlists = ["red", "green", "blue"]
print(any(stringlists))  # * True

stringlists = ["red", "", "orange"]
print(any(stringlists))  # * True

# todo Validate a list of conditions

required_fields = ["username", "email", "password"]

users = {"username": "susu", "email": "susu@gmail.com", "password": "12345"}

getresult = all(field in users and users[field] for field in required_fields)

print(getresult)  # * True

# ? Explaination
# ? 'username' in users = True
# ? users['username'] = susu (truthy) = True

required_fields = ["username", "email", "password"]

users = {"username": "susu", "email": "", "password": "12345"}

getresult = all(field in users and users[field] for field in required_fields)

print(getresult)  # ! False
