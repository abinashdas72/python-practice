import yaml
with open("config.yaml", "r") as file:
    data=yaml.safe_load(file)
    print(data["settings"]["debug"])
    print(data["settings"]["timeout"])