def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


testList = [1,3,4,5,6,743,23,54,535,2355]

print('')
print(bubble_sort(testList))
print(testList)
