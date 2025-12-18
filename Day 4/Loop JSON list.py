import json
with open("config.json", 'r') as file:
    content=json.load(file)
    for server in content["servers"]:
        print(f"Checking server: {server}")

