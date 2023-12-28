#!/usr/bin/env python3

import random

def qselect(i:int, a:list)->int:
    if a == []:
        return []
    idx = random.randint(0, len(a) - 1)
    pivot = a[idx]

    a[0], a[idx] = a[idx], a[0]

    left = [x for x in a if x < pivot]
    len_left = len(left)
    if len_left == i - 1:
        return pivot
    elif len_left < i - 1:
        right = [x for x in a[1:] if x >= pivot]
        return qselect(i - len_left - 1, right)
    else:
        return qselect(i,left)

if __name__ == "__main__":
    print(qselect(4, [4, 6, 19, 8, 10]))
