def is_even( i ):
    remainder = i % 2
    return remainder == 0

print("All numbers betweenn 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i ,"even")
    else:
        print(i, "odd")



def g(x):
    def h():
        x = 'abc'
    x = x+1
    print('g: x =', x)
    h()
    return x
x = 3
z = g(x)
print(z)


def sq(func, x):
    y = x**2 
    return func(y)

def f(x):
    return x ** 2

calc = sq(f, 2)
print(calc)
