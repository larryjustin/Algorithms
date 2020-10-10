from collections import defaultdict
# Helpful resources:
# https://www.geeksforgeeks.org/topological-sorting/
# https://stackoverflow.com/questions/47192626/deceptively-simple-implementation-of-topological-sorting-in-python


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


# print("Should return -> [0, 1, 2, 3, 4, 5, 6, 7] \t", order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print("Should return -> [0, 1, 2, 4, 3, 5, 6, 7] \t", order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
# print("Should return -> None \t\t\t\t\t\t", order(4, [(0,1), (1,2), (2,1), (2,3)]))
# print("Should return -> [0, 1, 2, 3, 4] \t\t\t", order(5, [(0,1), (1,2), (2,3), (3,4)]))
# print("Should return -> [0, 1, 2, 3, 4] \t\t\t", order(5, []))
# print("Should return -> None \t\t\t\t\t\t", order(1, [(0,0)]))
