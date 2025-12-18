import yaml
required_keys=["env", "region", "servers", "settings"]
with open("config.yaml", "r") as file:
    data=yaml.safe_load(file)
    for key in required_keys:
        if key not in data:
            print(f"{key} is missing")