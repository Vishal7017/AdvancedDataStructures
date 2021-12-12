def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, (b-1))

def fact(n):
    if n == 1:
        return 1

    else:
        return n * fact(n-1)