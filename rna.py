from heapq import *
from collections import defaultdict



def kbest(rna, key):
    def _kbest(i,j):
        def try_binary(s,p,q):
            if p < len(pk[i,s]) and q < len(pk[s+1,j]) and (s,p,q) not in visited:
                heappush(h,(- (pk[i,s][p][0] + pk[s+1,j][q][0]),(s,p,q)))
                visited.add((s,p,q))

        def push_unary(p):
            if p < len(pk[i+1,j-1]):
                heappush(h, (- (pk[i+1,j-1][p][0]+1),(p,)))

        if (i,j) in pk:
            return pk[i,j]

        if i==j:
            pk[i,j] = [(0,'.')]
            return 0
        elif j == i-1:
            pk[i,i-1] = [(0,'')]
            return 0
        h = []
        visited = set()
        for s in range(i,j):
            _kbest(i,s)
            _kbest(s+1,j)
            try_binary(s, 0,0)

        if rna[i]+rna[j] in a_set:
            _kbest(i+1,j-1)
            push_unary(0)

        found = 0
        while found < key:
            if h == []:
                break
            score, indices = heappop(h)
   
            try:
                s,p,q = indices
                result = (-score, "%s%s" % (pk[i,s][p][1],pk[s+1,j][q][1]))

                if result not in pk[i, j]:
                    pk[i, j].append(result)
                    found += 1

                try_binary(s,p+1,q)
                try_binary(s,p,q+1)
            except:
                p = indices[0]
                result = (-score, "(%s)" % pk[i+1,j-1][p][1])

                if result not in pk[i,j]:
                    pk[i, j].append(result)
                    found += 1
                push_unary(p+1)

    pk = defaultdict(list)
    past = {}
    n = len(rna)
    _kbest(0,n-1)
  
    return _kbest(0,n-1)


def total(rna):
    def _total(i, j):
        if(i, j) in opted:
            return opted[i,j]

        counter = 0
        for key in range(i, j):
            if rna[j] + rna[key] in a_set:
                counter += _total(i, key-1) * _total(key+1, j-1)
        counter += _total(i, j-1)
        opted[i,j] = counter

        return counter
    opted = defaultdict(int)
    n = len(rna)

    for i in range(n):
        opted[i, i] = 1
        opted[i, i-1] = 1

    return _total(0, n-1)


def best(rna):  
      
    
    def solution(i, j):
        if i == j:
            return "."
        if i > j: 
            return ""
        key = back[i, j]
        if key == -1:
            return "(%s)" % solution(i+1, j-1)
        else:
            return solution(i, key) + solution(key+1, j)

    def _best(i, j):
        if (i, j) in opted:
            return opted[i, j]
        curr = -1
        for key in range(i, j):
            if _best(i,key) + _best(key+1, j) > curr:
                curr = max(curr, _best(i,key)+ _best(key+1, j))
                back[i, j] = key
            
        if rna[i] + rna[j] in a_set:
            if _best(i+1, j-1) + 1 > curr:
                curr = _best(i+1, j-1) +1
                back[i, j] =  -1
            
        opted[i,j] = curr
        return curr

    opted = defaultdict(int)
    back = {}
    n = len(rna)
    for i in range(n):
        opted[i, i] = 0
        opted[i, i-1] = 0
    return _best(0, n-1), solution(0, n-1)




a_set = set(['AU', 'UA', 'CG', 'GC', 'GU', 'UG'])
