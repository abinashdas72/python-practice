import json
with open("config.json", 'r') as file:
    content=json.load(file)
    print(content["env"])
    print(content["region"])

