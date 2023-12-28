from collections import defaultdict
import copy
from time import time


def insert_vertex(n, vert, bit):
    if vert == -1:
        return bit + 1
    else:
        return bit + 2 ** (n - vert)


def remove_vertex(n, vert, bit):
    if vert == -1:
        return bit - 1
    else:
        return bit - 2 ** (n - vert)


def tsp(n, edges):
    graph = defaultdict(dict)
    for (x, y, z) in edges:
        graph[x][y] = z
        graph[y][x] = z
        if x == 0:
            graph[-1][y] = z
            graph[y][-1] = z
        if y == 0:
            graph[x][-1] = z
            graph[-1][x] = z

    opt = defaultdict(dict)
    back = defaultdict(dict)

    def tsp_helper(visited_bits, i):
        if visited_bits == 2**n and i == 0:
            return 0
        if i in opt[visited_bits]:
            return opt[visited_bits][i]
        min_cost = float("inf")
        for v in range(n):
            if 2 ** (n - v) & visited_bits != 0:
                if v != i and v in graph[i]:
                    new_visited_bit = remove_vertex(n, i, visited_bits)
                    temp = tsp_helper(new_visited_bit, v)
                    if temp is not None and min_cost > temp + graph[v][i]:
                        min_cost = temp + graph[v][i]
                        back[visited_bits][i] = v

        if min_cost == float("inf"):
            opt[visited_bits][i] = None
        else:
            opt[visited_bits][i] = min_cost
        return opt[visited_bits][i]

    def solution(visited_bits, i):
        if visited_bits == 2**n and i == 0:
            return [0]
        vertex = back[visited_bits][i]
        new_visited = remove_vertex(n, i, visited_bits)
        if i == -1:
            i = 0
        return solution(new_visited, vertex) + [i]

    vert_bit = 0
    for i in range(n):
        vert_bit = insert_vertex(n, i, vert_bit)
    vert_bit = insert_vertex(n, -1, vert_bit)

    return tsp_helper(vert_bit, -1), solution(vert_bit, -1)


