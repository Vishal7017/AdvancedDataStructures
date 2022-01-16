#Logarithmic Complexity

def intToStr(i):
    digits = '0123456789'
    if i ==0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10]+result
        i = i//10
    return result

print(intToStr(233))

#Log(n)

 
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

#O(n)

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1)

#O(n)