def reverse_string(string_input):
    max_range = len(string_input)
    string_output = ""
    while max_range > 0:
        string_output = string_output + string_input[(max_range - 1)]
        max_range = max_range - 1


    return string_output


print(reverse_string(input("Enter a string: ")))
