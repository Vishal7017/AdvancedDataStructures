#Iterative
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_1 = fib_ii
            fib_ii = tmp+fib_ii
        return fib_ii

#Recursive

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)