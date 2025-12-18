import os
variable_check=input("Please enter your variable: ")
if variable_check in os.environ:
    print(os.environ[variable_check])
else:
    print(f"File {variable_check} not found")