number = int(input("Guess a number"))
sum_num=0
for num in range(1,number+1):
    sum_num= sum_num + num
print(f"SUm of numbers till {number} is : - {sum_num}")