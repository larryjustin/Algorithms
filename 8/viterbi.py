from collections import defaultdict
# Helpful resources:
# https://people.eecs.berkeley.edu/~vazirani/algorithms/chap3.pdf


# code from topol:
def order(n, edges):
    graph = defaultdict(list)
    degrees = defaultdict(int)
    seen = set()
    result = []
    for (u, v) in edges:
        degrees[v] += 1
        graph[u].append(v)

    for i in range(0, n):
        if degrees[i] == 0:
            seen.add(i)

    while len(seen) > 0:
        c = seen.pop()
        result.append(c)
        for n in graph[c]:
            degrees[n] -= 1
            if degrees[n] == 0:
                seen.add(n)
# this ensures the word "None" is returned
    if sum(degrees.values()) > 0:
        return None

    return result
# :end code from topol


def longest(n, edges):
    path = order(n, edges)
    num = (0, 0)
    graph = defaultdict(list)
    result = defaultdict(int)
# set default value to -1
    back = defaultdict(lambda: -1)
    for (u, v) in edges:
        graph[u].append(v)

    for u in path:
        for v in graph[u]:
            if result[u] + 1 > result[v]:
                result[v] = result[u] + 1
                back[v] = u
                if result[v] > num[0]:
                    num = result[v], v

    return num[0], solutions(back, num[1]) + [num[1]]


def solutions(back, num):
    if back[num] == -1:
        return []
    return solutions(back, back[num]) + [back[num]]


# print("Should Return -> (5, [0, 2, 3, 4, 5, 6]) \t\t", longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print("Should Return -> (5, [0, 2, 4, 3, 5, 6]) \t\t", longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
# print("Should Return -> (7, [0, 1, 2, 4, 3, 5, 6, 7]) \t", longest(8, [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (4, 3), (3, 5), (4, 5), (5, 6), (5, 7), (6, 7)]))
