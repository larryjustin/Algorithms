import heapq


def ksmallest(k, lst):
    if not lst or k < 1 or k >= len(lst):
        return
    heap = []
    k = k - 1
    for item in lst:
        item = -item
        if len(heap) <= k:
            heapq.heappush(heap, item)
        else:
            heapq.heappushpop(heap, item)
#    return sorted(heap, key=lambda x: -x)
#    return list(map(lambda x: -x, heap))
    return sorted(map(lambda x: - x, heap))


# print("Should output [2, 3, 5, 7] -> ", ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
# print("Should output [1, 2, 3] -> ", ksmallest(3, range(1000000, 0, -1)))
