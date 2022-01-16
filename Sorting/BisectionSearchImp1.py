#Bisection Search Implementation 1

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:

        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)
            
    

L = [23, 34, 45, 56, 67, 78]
e = 34

print(bisect_search1(L, e))