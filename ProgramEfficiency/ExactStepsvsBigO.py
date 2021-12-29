#computes factorial

def fact_iter(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer



#Law of Addition for O()
# used with sequential statements

for i in range(n):
    print('a')

for j in range(n*n):
    print('b')

 #O(n2)


#Law of Multiplication for O()
# used with nested statements/loops

for i in range(n):
    for j in range(n):
        print('a')