#!/usr/bin/env python3

import math, random, time

def _qselect(k, a): # modified quick select to handle tie-breaking cases
    pindex = random.randint(0, len(a)-1)
    a[0], a[pindex] = a[pindex], a[0]
    pivot = a[0]
    left = [x for x in a if x < pivot]
    mid = [x for x in a[1:] if x == pivot]
    lleft, lmid = len(left), len(mid)
    if k <= lleft:
        return _qselect(k, left)
    elif k <= lleft+lmid+1:
        return pivot, lleft # lleft elements strictly smaller than pivot
    else:
        right = [x for x in a[1:] if x > pivot]
        diff = lleft+1+lmid
        r0, r1 = _qselect(k-diff, right)
        return r0, r1+diff

def _find(lst, q, k):
    difflist = [round(math.fabs(x-q), 10) for x in lst] # floating point: round to .1
    maxdiff, k_small = _qselect(k, difflist)
    rest = k - k_small # quota for those on the boundary
    for x, diff in zip(lst, difflist):
        if diff < maxdiff: # strictly smaller than threshold, always take
            yield x
        elif diff == maxdiff and rest > 0: # on boundary: only take the first rest of them
            yield x
            rest -= 1

find = lambda l, w, k: list(_find(l, w, k)) # convert lazylist to list

if __name__ == "__main__":

   print(find([4,1,3,2,7,4], 5.2, 2)) # == [4,4])
   print(find([4,1,3,2,7,4], 6.5, 3)) # == [4,7,4])
   print(find([5,3,4,1,6,3], 3.5, 2)) # == [3,4])
