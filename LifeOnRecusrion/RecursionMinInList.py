def find_min(my_list, min=None):
    if not my_list:
        return min
    
    if not min or my_list[0] < min:
        min = my_list[0]

    return find_min(my_list[1:], min)

print(find_min([3,43,-2,4,3]) == -2)
print(find_min([100,22,12,12,324,12]) == 100)