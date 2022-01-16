def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


testList = [1,3,4,5,6,743,23,54,535,2355]

print('')
print(selection_sort(testList))
print(testList)
