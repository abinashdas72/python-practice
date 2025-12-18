import json
with open("config.json", "r") as file:
    data=json.load(file)
    timeout=data.get("settings", {}).get("timeout", 10)
    print(timeout)