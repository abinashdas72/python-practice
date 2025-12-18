import json
required_keys=["env", "region", "servers"]
with open("config.json", "r") as file:
    content=json.load(file)

    for key in required_keys:
        if key in content:
            print(f"The value for key :- {key}: {content[key]}")
        else:
            print(f"Missing key: {key}")