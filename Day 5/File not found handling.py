import yaml

try:
    filename=input("Please enter the file name:")
    with open(filename, "r") as file:
        data=yaml.safe_load(file)

except FileNotFoundError as exc:
    print(f"File not found: {exc}")