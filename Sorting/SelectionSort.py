def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


testList = [1,3,4,5,6,743,23,54,535,2355]

# print('')
# print(selection_sort(testList))
# print(testList)



#Selection Sort Recursive

def selection_sort2(A, i = None):
    '''Sort A[:i + 1]'''
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort2(A, i - 1)

#Helper Function for selection sort
def prefix_max(A, i):
    '''Return index of maximum in A[:i + 1]'''
    if i > 0:
        j = prefix_max(A, i -1)
        if A[i] < A[j]:
            return j
    return i

print('')
print(selection_sort2(testList))
print(testList)