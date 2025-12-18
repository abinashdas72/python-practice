try:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    div = number1 / number2

except ValueError as ve:
    print(ve)
except ZeroDivisionError as ve:
    print(ve)

else:
    print(number1)
    print(number2)
    print(div)