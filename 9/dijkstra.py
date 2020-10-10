from collections import defaultdict
from heapdict import heapdict


def shortest(n, edges):
    edge = defaultdict(list)
    heapd = heapdict()
    visited = set()
    back = defaultdict(lambda: -1)
    for (u, v, w) in edges:
        edge[u].append((v, w))
        edge[v].append((u, w))
    heapd[0] = 0
    while len(heapd) > 0:
        prev_node, cur_dist = heapd.popitem()
        visited.add(prev_node)
        if prev_node == n - 1:
            return cur_dist, goback(n, back)
        for (neighbor, cost) in edge[prev_node]:
            if neighbor not in visited:
                prev_cost = cur_dist + cost
                if (neighbor not in heapd.keys()) or (heapd[neighbor] > prev_cost):
                    heapd[neighbor] = prev_cost
                    back[neighbor] = prev_node


def goback(n, back):
    node = back[n-1]
    result = [n-1]
    while node != -1:
        result.append(node)
        node = back[node]
    result.reverse()
    return result


print("Correct output: (4, [0,1,2,3]) \t->\t ", shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
print("Correct output: None \t\t\t->\t ", shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6),]))
print("Correct output: None \t\t\t->\t ", shortest(4, [(0,1,1), (2,3,1)]))
