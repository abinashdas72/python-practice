list1 = [1,2,3,4,5,6,7,8,9, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)