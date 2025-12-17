list1 = [1,2,3,4,5,6,7,8,9]
largest_num = list1[0]
for num in list1:
    if num > largest_num:
        largest_num = num
print(f"The largest number is {largest_num}")