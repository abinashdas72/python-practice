servers = {
    "web01": {"ip": "10.0.0.5", "status": "running"},
    "db01": {"ip": "10.0.0.10", "status": "stopped"}
}

print(servers["db01"]["ip"])
print(servers["web01"]["status"])