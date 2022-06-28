#Double Array values
#Space complexity O(N)
def double_array1(input_array):
    length = len(input_array)
    double_array = [0] * length
    for i in range(length):
        double_array[i] = input_array[i]*2
    return double_array


#Space complexity O(1)

def double_array2(input_array):
    for i in range(len(input_array)):
        input_array[i] *= 2
    return input_array

print(double_array1([1,2,3,4,5,6]))
print(double_array2([1,2,3,4,5,6]))