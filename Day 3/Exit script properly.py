import sys
number=int(input("Enter a number: "))
if number >= 0:
    sys.exit(0)
else:
    print("number is negative")
    sys.exit(1)