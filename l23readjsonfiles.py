import json
import os

# * Reading Json from a String (loads)

json_string = '{"name":"John Doe","age":23,"isStudent":true}'
# print(json_string) # ? di lol lae phat loa ya tal
# print(json_string["name"])  # ! TypeError: string indices must be integers, not 'str'

datas = json.loads(json_string)  # ? di lol lae phat loa ya tal
print(datas)
print(datas["name"])  # ? John Doe
print(datas["age"])  # ? 23

# * Reading a simple JSON file (load)


def readjson(filename):
    with open(filename, "r") as file:
        datas = json.load(file)
    return datas


getsimplejson = readjson("files/file8.json")
print(getsimplejson)

print(getsimplejson["name"])  # ? John Doe
print(getsimplejson["age"])  # ? 23
print(getsimplejson["isStudent"])  # ? False
print(getsimplejson["hasCar"])  # ? True
print(getsimplejson["hobbies"][0])  # ? reading
print(getsimplejson["hobbies"][1])  # ? traveling


# * Read a JSON Array File (load for json format)

getarrayjsons = readjson("files/file9.json")
print(getarrayjsons)

for getarrayjson in getarrayjsons:
    print(
        f"Name: {getarrayjson["name"]}, Age: {getarrayjson["age"]}, isStudent: {getarrayjson["isStudent"]}, has Car: {getarrayjson["hasCar"]} ,Hobbies: {getarrayjson["hobbies"][0]} and {getarrayjson["hobbies"][1]}"
    )

# * Reading a complex JSON File (load for json format)

getcomplexjsons = readjson("./files/file10.json")

print(getcomplexjsons)
print(getcomplexjsons["company"])  # ? Apple
get_product = getcomplexjsons["product"]
print(get_product[0]["name"])
print(get_product[0]["price"])
print(get_product[0]["features"][0])
print(get_product[0]["features"][1])
print(get_product[0]["features"][2])
print(get_product[1]["name"])
print(get_product[1]["price"])
print(get_product[1]["features"][0])
print(get_product[1]["features"][1])
print(get_product[1]["features"][2])

# todo Error Handling (Check file exit or not)

try:
    with open("files/file10.json", "r") as file:
        datas = json.load(file)
except FileNotFoundError as e:
    print("Error: File not found.", str(e))
except json.JSONDecodeError as e:
    print("Error: Invalid JSON format!", str(e))
else:
    print(datas)

getfile = "files/file100.json"  #! ma shi tat file ko san tar

if not os.path.isfile(getfile):
    print(f"Error: File{getfile} does not exit.")
else:
    with open(getfile, "r") as file:
        datas = json.load(file)
        print(datas)
