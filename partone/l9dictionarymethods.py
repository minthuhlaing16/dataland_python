lady = {"name": "Hla Hla Win", "age": 34, "city": "Yangon"}

print(lady)  # {'name': 'Hla Hla Win', 'age': 34, 'city': 'Yangon'}
print(lady.get("name"))  # Hla Hla Win
print(lady.get("country"))  # None
print(lady.get("country", "America"))  # America

print(lady.keys())  # dict_keys(['name', 'age', 'city'])
print(list(lady.keys()))  # ['name', 'age', 'city']
print(list(lady.keys())[0])  # name
print(list(lady.keys())[1])  # age

print(lady.values())  # dict_values(['Hla Hla Win', 34, 'Yangon'])
print(list(lady.values()))  # ['Hla Hla Win', 34, 'Yangon']
print(list(lady.values())[0])  # Hla Hla Win
print(list(lady.values())[1])  # 34

print(
    lady.items()
)  # dict_items([('name', 'Hla Hla Win'), ('age', 34), ('city', 'Yangon')])
print(list(lady.items()))  # [('name', 'Hla Hla Win'), ('age', 34), ('city', 'Yangon')]
print(list(lady.items())[0])  # ('name', 'Hla Hla Win')
print(list(lady.items())[0][0])  # name
print(list(lady.items())[0][1])  # Hla Hla Win
print(list(lady.items())[1][0])  # age
print(list(lady.items())[1][1])  # 34
print(list(lady.items())[2][0])  # city
print(list(lady.items())[2][1])  # Yangon


lady.update({"age": 20, "gender": "Female"})
print(lady)  # {'name': 'Hla Hla Win', 'age': 20, 'city': 'Yangon', 'gender': 'Female'}

lady.pop("age")
print(lady)  # {'name': 'Hla Hla Win', 'city': 'Yangon', 'gender': 'Female'}

lady.clear()
print(lady)  # {}


girl = {"name": "susu", "age": 12}
print(girl)  # {'name': 'susu', 'age': 12}

# print(girl.pop()) # TypeError: pop expected at least 1 argument, got 0

print(girl.pop("name"))  # susan
print(girl)  # {'age': 12}

boy = {"name": "Mr White", "age": 32, "city": "Yangon"}
print(boy)  # {'name': 'Mr White', 'age': 32, 'city': 'Yangon'}

boy.popitem()  # nout sone ka del tar

print(boy)  # {'name': 'Mr White', 'age': 32}

man = boy.copy()
print(man)  # {'name': 'Mr White', 'age': 32}
