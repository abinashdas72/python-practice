
try:
    filename=input("Please enter the file name:")
    with open(filename, "r") as file:
        data=file.read()

except FileNotFoundError as exc:
    print(f"File not found: {exc}")
else:
    print(data)
finally:
    print("Cleanup done")