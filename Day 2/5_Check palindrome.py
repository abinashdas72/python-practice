from Reverse_a_string import reverse_string

string_input = input("Enter a string  : ")
string_reverse = reverse_string(string_input)
if string_input == string_reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")
