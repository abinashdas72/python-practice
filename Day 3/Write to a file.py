file=open("sample.log", 'w')
file.write("INFO: Application started \n")
file.write("INFO: Connecting to DB \n")
file.write("ERROR: Connection failed \n")
file.write("INFO: Retrying \n")
file.write("INFO: Application running \n")
file.close()

with open("sample.log", "a") as file:
    file.write("INFO: Application still running \n")

with open("sample.log", "r") as file:
    print(file.read())