import yaml
with open("config.yaml", "r") as file:
    data=yaml.safe_load(file)
    for server in data["servers"]:
        print(f"Pinging {server}")