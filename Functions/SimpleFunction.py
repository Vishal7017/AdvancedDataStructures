L = ["life", "answer", 42, 0]

for thing in L:
    if thing==0:
        L[thing] = "universe"
    # elif thing==42:
    #     L[1] = "everything"


print(L)