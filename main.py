import json

print("Hello people")

recent_number = 10

my_json = {
    "name" : "Sijan",
    "age": 26,
    "recent_number" : recent_number
}
recent_number +=1

with open("hello.json", "w") as file:
    json.dump(my_json, file, indent=4)