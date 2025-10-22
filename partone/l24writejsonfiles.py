import json

# todo Write a simple JSON file

datas = {
    "title": "Python FastAPI Batch 1",
    "price": 23.44,
    "packages": ["FastAPI", "Jinja2", "OpenAi", "Websocket"],
}

with open("files/file11.json", "w") as file:
    # json.dump(datas, file) #? parameter 2 khu
    # json.dump(datas, file, indent=4)  # ? indent ba lout char ma lae pay tar
    json.dump(
        datas, file, indent=4, sort_keys=True
    )  # ? sort_keys ==> A to Z key ko si tar
    print("Successfully Created...")

#! ==> Error Handling

try:
    invaliddatas = {"numbers": {1, 2, 3}}  # * Set is not JSON-serializable
    with open("files/fileerror.json", "w") as file:
        json.dump(invaliddatas, file)
except TypeError as e:
    print("Error: Type Error: ", str(e))
