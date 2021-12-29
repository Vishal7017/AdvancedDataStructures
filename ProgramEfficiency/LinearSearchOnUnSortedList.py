def linear_search(L, e):
    found = False
    for i in ragne(len(L)):
        if e == L[i]:
            found = True
    return found


#must look though all elements to decide it's nont there