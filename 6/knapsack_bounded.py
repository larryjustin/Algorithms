

def best(weight, item):
    opt = [[0 for _ in range(0, weight + 1)] for _ in range(0, len(item) + 1)]
    tpo = [[0 for _ in range(0, weight + 1)] for _ in range(0, len(item) + 1)]

    for i, (w, v, c) in enumerate(item):
        i += 1
        for x in range(1, weight + 1):
            for j in range(min(c, x // w) + 1):
                if x >= j * w and opt[i][x] < opt[i - 1][x - j * w] + j * v:
                    opt[i][x] = opt[i - 1][x - j * w] + j * v
                    tpo[i - 1][x] = j
    return opt[len(item)][weight], knapsack(weight, len(item) - 1, item, tpo)


def knapsack(w, i, item, tpo):
    if i < 0:
        return []
    w2 = w - item[i][0] * tpo[i][w]
    return knapsack(w2, i - 1, item, tpo) + [tpo[i][w]]


"""
print("Should result in (5, [0, 1]) -> ", best(3, [(2, 4, 2), (3, 5, 3)]))
print("Should result in (15, [2, 1]) -> ", best(3, [(1, 5, 2), (1, 5, 3)]))
print("Should result in (15, [1, 2]) -> ", best(3, [(1, 5, 1), (1, 5, 3)]))
print("Should result in (130, [6, 4, 1]) -> ", best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print("Should result in (236, [6, 7, 3, 7, 2]) -> ", best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
"""