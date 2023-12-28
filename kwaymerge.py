import math
import heapq

def kmerge(lists):
    final_list = []
    print(lists)
    heap = [(mylst[0], i, 0) for i, mylst in enumerate(lists) if mylst]
    print(heap)
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        final_list.append(val)
        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return final_list
    
    
def kmergesort (arr, k):
    if len(arr) == 1:      
        return arr
    size = math.ceil(len(arr)/k)
    arr = [kmergesort(arr[i:i+size], k) for i in range(0, len(arr), size)]  
    return kmerge(arr)

print(kmergesort([4,1,5,2,6,3,7,10], 5))