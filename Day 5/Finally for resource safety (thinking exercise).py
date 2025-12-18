import sys
file = None
try:
    filename = input("Please enter the file name:")
    file=open(filename, 'r')
    data=file.read()
    sys.exit(1)

except FileNotFoundError as exc:
    print(f"File not found: {exc}")
except NameError as exc:
    print(f"NameError: {exc}")

else:
    print(data)

finally:
    if file:
        file.close()
        print("File closed safely")