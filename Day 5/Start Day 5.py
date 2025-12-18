try:
    number_input = input('Enter a number:')
    number = int(number_input)
except ValueError as exc:
    print(f"Error: {exc}, the input number is not valid")
else:

    print(f"The input number is valid")