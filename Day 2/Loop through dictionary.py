server = {
    "name": "web01",
    "ip": "10.0.0.5",
    "status": "running"
}

for key in server:
    print(f"{key} : {server[key]}")