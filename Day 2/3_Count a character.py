string_input = input("Enter a string: ")
char_input = input("Enter a Character which you need count of: ")
if char_input in string_input:
    count =  string_input.count(char_input)
    print(f"{char_input} is repeated {count} times")
else:
    print(f"{char_input} is not repeated")