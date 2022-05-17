def multiplication(num1, num2):
    result = 0
    for count in range(0, num2):
        result += num1
    return result

print(multiplication(4,5))
print(multiplication(12,23))
print(multiplication(15,2))


def multiplication(num1, num2):
    result = 0
    for count in range(0, num2):
        result += num1
    return result

def multiplication2(num1, num2):
    if num1 == 0 or num2 ==0:
        return 0
    return num1 + multiplication2(num1, num2-1)
    