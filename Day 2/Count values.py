services = ["nginx", "ssh", "docker", "ssh", "nginx"]
count_services = {}
for service in services:
    if service in count_services:
        count_services[service] += 1
    else:
        count_services[service] = 1


print(count_services)