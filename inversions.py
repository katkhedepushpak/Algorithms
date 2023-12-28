inversions = 0
def merging(left_a, right_a):
    temp_array = []
    x = y = 0
    mid = len(left_a)
    while x < len(left_a) and y < len(right_a):
        if left_a[x] < right_a[y]:
            temp_array.append(left_a[x])
            x += 1
        else:
            temp_array.append(right_a[y])
            temp = mid - x
            global inversions
            inversions = inversions + temp
            y += 1
    temp_array.extend(left_a[x:])
    temp_array.extend(right_a[y:])
    return temp_array


def mergesort(Arr):
    n = len(Arr)
    if n == 1:
        return Arr
    middle = n // 2
    left_array = mergesort(Arr[:middle])
    right_array = mergesort(Arr[middle:])

    return merging(left_array, right_array)


A = [2, 4, 1, 3]
mergesort(A)
print(inversions)
