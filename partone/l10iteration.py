# looping === iteration
# for in loop
# iteration a list
names = ["John Doe", "Bob", "Alice", "Susan", "Alex", "The Rock"]
for name in names:
    print("Hi " + name)

# iteration a String
message = "Hello John?"
print(len(message))
for msg in message:
    print(msg)

# iteration a dictionary
students = {"name": "Susan", "age": 32, "city": "Mandalay"}
print(students)
print(students.items())

# for key in students:
#     print(key)

# for key in students.items():
#     print(key)

for key, value in students.items():
    print(key, "=", value)

# for key, value in students:
#     print(key, "=", value) ==> error

# for key in students:
#     print(key, students[key])


# range() in for in loop

for x in range(10):
    print(x)  # 0 to 9

print(f"Outside value of x is: {x}")  # Outside value of x is: 9


for y in range(1, 10):
    print(y)
print(f"Outside value of y is : {y}")

for p in range(1, 10, 2):
    print(p)
print(f"Outside value of p is {p}")


# break and continue

for i in range(10):
    if i == 5:
        break  # Exit the loop if i is equal to 5
    print(i)  # 0 to 4
print(f"Outside value of i is {i}")  # Outside value of i is 5


for q in range(10):
    if q == 5:
        continue  # Skip number 5
    print(q)  # 0 1 2 3 4 6 7 8 9
print(f"Outside value of q is : {q}")


for j in range(20):
    if j % 2 == 0:
        continue  # Skip even number
    print(j)  # 1 3 5 7 9 ...19
print(f"Outside value of j is: {j}")


# Nested Loops
staffs = [
    ["aung aung", "kyaw kyaw", "zaw zaw"],
    ["susu", "nunu", "yuyu"],
    ["thidar", "nilar", "yupar"],
]

# for staff in staffs:
#     print(staff)


# for staff in staffs:
#     for people in staff:
#         print(people)


# for staff in staffs:
#     for people in staff:
#         print(people)
#         print()


# for staff in staffs:
#     for people in staff:
#         print(people)
#     print()


# for staff in staffs:
#     for people in staff:
#         print(people, end=" , ")


# for staff in staffs:
#     for people in staff:
#         print(people, end=" ")
#     print()


# while loop
idx = 0
while idx < 10:
    print(f"Index: {idx}")
    idx += 1
print(f"Outside value of idx is : ", idx)  # Outside value of idx is :  10

count = 0
while count < 10:
    count += 1
    print(f"Count: {count}")
print(f"Outside value of count is {count}")

paints = ["red", "green", "blue"]
print(paints)
print(enumerate(paints))  # <enumerate object at 0x7fe73d283740>

for idx, paint in enumerate(paints):
    print(idx, paint)


index = 0
while index < len(paints):
    print(index, paints[index])
    index += 1


# ==> break,continue
# while True:
#     username = input("Enter username: ")
#     if username == "aung aung":
#         print("Welcome Aung Aung..")
#         break
#     else:
#         continue

# ==> not , and
initnum = False

while not initnum:
    lucky_number = input("Enter your lucky number: ")
    if lucky_number.isdigit() and int(lucky_number) > 0:
        print(f"Your lucky number is ==> {lucky_number}")
        initnum = True
    else:
        print("Invalid Number...")
