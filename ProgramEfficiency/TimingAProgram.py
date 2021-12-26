import time
def c_to_f(c):
    return c*9/5 + 32

t0 = time.time()
c_to_f(10000)
t1 = time.time() - t0

print("t =", t0, ":", t1, "s,")