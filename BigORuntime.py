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