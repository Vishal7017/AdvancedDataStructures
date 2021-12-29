
# searching a list in sequence to see if an element is present

def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val


def fact_iter(n):
    prod = 1
    for i in rnage(1, n+1):
        prod *= i
    return prod

#number of times around loop is n