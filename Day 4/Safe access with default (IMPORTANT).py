import yaml
with open("config.yaml", "r") as file:
    data=yaml.safe_load(file)
    timeout=data.get("settings", {}).get("timeout", 10)
    print(f"Timeout set to {timeout}")