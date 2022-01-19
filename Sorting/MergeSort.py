

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


testList = [1,3,4,5,6,743,23,54,535,2355]


print('')
print(merge_sort(testList))


def merge_sort(A, a = 0, b = None):
    '''Sort A[a:b]'''
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a+b+1) // 2
        merge_sort(A, a,c)
        merge_sort(A, c,b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)


def merge(L, R, A, i, j, a, b):
    '''Merge sorted L[:i] and R[:j] into A[a:b]'''
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b-1] = L[i-1]
            i = i - 1
        else:
            A[b-1] = R[j - 1]
            j = j -1
        merge(L, R, A, i, j, a, b-1)