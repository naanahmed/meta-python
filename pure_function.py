my_nums = [1,2,3,4,5,6,7,8,9,10]

def add_nums(list, num):
    new_nums = list.copy()
    new_nums.append(num)
    return new_nums

new_my_nums = add_nums(my_nums, 11)

print(my_nums)
print(new_my_nums)
