def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)


def power_set2(set):
    power_set_size = 2**len(set)
    result = []

    for bit in range(0, power_set_size):
        sub_set = []
        for binary_digit in range(0, len(set)):
            if((bit & (1 << binary_digit)) > 0):
                sub_set.append(set[binary_digit])
        result.append(sub_set)
    return result

print(power_set2(["a","b","c","d","e"]))