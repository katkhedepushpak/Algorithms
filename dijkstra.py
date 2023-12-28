# from heapq import heapify, heappop, heappush
# from collections import defaultdict


def shortest(n, edges):

    from heapq import heapify, heappop, heappush
    from collections import defaultdict
    
    out_edges = defaultdict(list)
    h = [(0, 0)]
    
    for s, e, distance in edges:
        out_edges[s].append((distance, e))
        out_edges[e].append((distance, s))

    back = {i: -1 for i in range(n)}
    distances = {i: float("inf") for i in range(n)}
    distances[0] = 0

    while h:
        till_distance, node = heappop(h)
        for next_distance, end in out_edges[node]:
            if next_distance + distances[node] < distances[end]:
                distances[end] = next_distance + distances[node]
                heappush(h, (distances[end], end))
                back[end] = node

    # print(distances)
    # print(backtrack)
    lst_res = []
    n -= 1
    d = distances[n]

    while n != -1:
        lst_res.append(n)
        n = back[n]

    lst_res.reverse()

    return (d, lst_res) if d != float("inf") else None
