def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


#By sorting method
def kth_largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]


#By Heaps Prioity queue
import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)