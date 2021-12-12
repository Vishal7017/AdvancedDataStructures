def q_and_r (x,y):
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = q_and_r(4,5)

print((quot, rem))

x = 50
y = 60
print(x)
print(y)
temp = x
x = y
y = temp
print(x)
print(y)

(x, y) = (y, x)

print((x, y))