from random import randint

def sorted(A):
    if len(A) > 0:
        sorted(A[0])
        print(A[1])
        sorted(A[2])

def _insert(n, Arr):
    if Arr == []:
        return [[], n, []]
    elif n < Arr[1]:
        Arr[0] = insert(n, Arr[0])
        return Arr
    elif n > Arr[1]:
        Arr[2] = insert(n, Arr[2])
        return Arr


def _search(key, Arr):
    if Arr == []:
        return []
    else:
        if key == Arr[1]:
            return Arr
        elif key > Arr[1]:
            return _search(key, Arr[2])
        else:
            return _search(key, Arr[0])


def insert(elem, Arr):
    if search(elem, Arr):
        return "The node is already in the tree"
    else:
        return _insert(elem, Arr)


def search(elem, Arr):
    if _search(elem, Arr) == []:
        return False
    else:
        return True


def sort(Arr):
    if not Arr:
        return []
    else:
        ind = randint(0, len(Arr) - 1)
        Arr[ind], Arr[0] = Arr[0], Arr[ind]

        left_array = []
        right_array = []
        for i in range(1, len(Arr)):
            if Arr[i] < Arr[0]:
                left_array.append(Arr[i])
            else:
                right_array.append(Arr[i])
        return [sort(left_array)] + [Arr[0]] + [sort(right_array)]
