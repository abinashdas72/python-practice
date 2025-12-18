try:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    div = number1 / number2

except ValueError as ve:
    print("Error: Invalid input")
except ZeroDivisionError as ve:
    print("Error: the number can't be zero!")

else:
    print(f"The divided number is: {div}")
finally:
    print("Execution completed")