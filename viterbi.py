from collections import defaultdict
def longest(n, edges): 

    dictionary = {i: [] for i in range(n)}

    s = set(range(n))
    for i, j in edges:
        dictionary[i].append(j)
        if j in s:
            s.remove(j)
    s = list(s)

    count = {i: 0 for i in range(n)}
    backtrack = {i: -1 for i in range(n)}

    ind = 0
    max_path = 0
    max_node = -1

    while ind < len(s):
        for i in dictionary[s[ind]]:
            s.append(i)
            if count[i] < count[s[ind]] + 1:
                count[i] = count[s[ind]] + 1
                backtrack[i] = s[ind]
                if count[i] > max_path:
                    max_node = i
                    max_path = count[i]
        ind += 1
        
    lst = []

    while max_node != -1:
        lst.append(max_node)
        max_node = backtrack[max_node]
    return max_path, list(reversed(lst))

