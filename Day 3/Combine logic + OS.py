import os
filename = input("Enter a filename")
file_exists=os.path.isfile(filename)
if file_exists:
    print(f"File size is {os.path.getsize(filename)}")
else:
    print(f"File {filename} is not found")