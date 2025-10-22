# Method - 1
student = {"name": "john doe", "age": 20, "city": "Yangon"}

print(student)  # {'name': 'john doe', 'age': 20, 'city': 'Yangon'}
print(student["name"])  # john doe

print(
    student.get("age")
)  # 20 ==> dot notation nae khaw loa ma ya buu .get("") so pee khaw ka tar


# Method - 2 dict()

staff = dict(name="aung aung", age=23, city="Mandalay")
print(staff)  # {'name': 'aung aung', 'age': 23, 'city': 'Mandalay'}
print(staff["name"])  # aung aung
print(staff.get("age"))  # 23

# print(student["country"]) # KeyError: 'country'
# print(staff["country"]) # KeyError: 'country'

print(student.get("country"))  # None
print(staff.get("country"))  # None

print(student.get("country", "Myanmar"))  # Myanmar
print(staff.get("country", "Thailand"))  # Thailand

print(student.get("age", 50))  # 20
print(staff.get("age", 50))  # 23


employee = {"name": "James Bond", "age": 23, "city": "washingtom"}

print(employee)  #  {'name': 'James Bond', 'age': 23, 'city': 'washingtom'}

# htet toe mal so yin
employee["email"] = "jamesbond@gmail.com"
print(
    employee
)  # {'name': 'James Bond', 'age': 23, 'city': 'washingtom', 'email': 'jamesbond@gmail.com'}

# twr del mal
del employee["city"]
print(employee)  # {'name': 'James Bond', 'age': 23, 'email': 'jamesbond@gmail.com'}

worker = dict(name="alice", age=23, city="Bago")
print(worker)  # {'name': 'alice', 'age': 23, 'city': 'Bago'}

worker["email"] = "alice@gmail.com"
print(
    worker
)  # {'name': 'alice', 'age': 23, 'city': 'Bago', 'email': 'alice@gmail.com'}

del worker["city"]
print(worker)  # {'name': 'alice', 'age': 23, 'email': 'alice@gmail.com'}
