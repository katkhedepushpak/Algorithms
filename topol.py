def get_zero_indegree(indegree, result, queue):
    temp_arr = []
    for elem in indegree:
        if indegree[elem] == 0 and elem not in queue and elem not in result:
            temp_arr.append(elem)
    return temp_arr

def order(n, edges):
    result = []

    nodes = [i for i in range(0, n)]

    indegree = dict(zip(nodes, [0]*n))

    for a, b in edges:
        indegree[b] += 1


    queue = []
    while len(result) != n:
        temp = get_zero_indegree(indegree, result, queue)
        queue.extend(temp)
        if queue == []:
            return None
        
        pr_node = queue.pop(0)
        for node in edges:
            if node[0] == pr_node:
                indegree[node[1]] -= 1
        result.append(pr_node)
    return result











if __name__ == "__main__":
    n, l = 1, [(1,1)]
    ans = order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print(ans)