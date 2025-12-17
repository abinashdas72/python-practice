count = 0
with open("sample.log", "r") as file:
    for line in file:
        if 'ERROR' in line:
            count += 1


print(f"The count of line containng ERROR is : {count}")