server = {
    "name": "web01",
    "ip": "10.0.0.5",
    "status": "running"
}

input_key=input("Enter a key")

if input_key in server:
    print(f"The value for key {input_key} is {server[input_key]}")
else:
    print(f"{input_key} is not present in the server")
