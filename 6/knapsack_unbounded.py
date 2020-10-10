

def best(weight, items):
    d = {0: [0, [0] * len(items)]}
    return knapsack(weight, items, d)


def knapsack(weight, items, d):
    if weight in d:
        return d[weight]
    result = d[0]
    for i in range(len(items)):
        if weight >= items[i][0]:
            [v, a] = knapsack(weight - items[i][0], items, d)
            v += items[i][1]
            a2 = list(a)
            a2[i] += 1
            if v > result[0]:
                result = [v, a2]
    d[weight] = result
    return result


"""
print("Should result in (5, [0, 1]) -> ", best(3, [(2, 4), (3, 5)]))
print("Should result in (15, [3, 0]) -> ", best(3, [(1, 5), (1, 5)]))
print("Should result in (15, [0, 3]) -> ", best(3, [(1, 2), (1, 5)]))
print("Should result in (7, [1, 1]) -> ", best(3, [(1, 2), (2, 5)]))
print("Should result in (114, [2, 4, 2]) -> ", best(58, [(5, 9), (9, 18), (6, 12)]))
print("Should result in (109, [1, 1, 7, 1]) -> ", best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
"""
