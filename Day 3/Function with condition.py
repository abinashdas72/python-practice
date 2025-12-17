def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


even=is_even(11)
if even == True:
    print("Even")
else:
    print("Odd")