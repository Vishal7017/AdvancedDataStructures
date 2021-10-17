def func_one(list):
    for element in list:
        print(element)
        if element % 2 == 0:
            print("EVEN STEVEN!")

def func_two(list):
    for element in list:
        for element2 in list:
            print(element, element2)


def func_three(list):
    print(list)
    for i in range(0, 100000):
        print(i)


def func_four(list):
    for element in list:
        print(element)

    for element2 in list:
        print(element * element)


def print_even_pairs(list):
    for element1 in list:
        for element2  in list:
            if (element1 + element2) % 2 == 0:
                print(element1, element2)

            

def find_max(list):
    max = list[0]
    for value in list:
        if value > max:
            max = value
    return max



def mystery_function(list, target):
    start_idx = 0
    end_idx = len(list) - 1

    while start_idx <= end_idx:
        mid = (start_idx + end_idx) // 2
        mid_value = list[mid]

        if mid_value == target:
            return mid
        
        if mid_value > target:
            end_idx = mid - 1
        else:
            start_idx = mid + 1
    raise ValueError("{0} is not in list".format(target))