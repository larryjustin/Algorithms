import heapq


def kmergesort(a, k):
    lst = len(a)
    if lst <= 1:
        return a
    delta = (lst - 1) // k + 1
    lsts = [kmergesort(a[i:i + delta], k) for i in range(0, lst, delta)]
    return list(heapq.merge(*lsts))


# https://docs.python.org/3/howto/sorting.html
# https://docs.python.org/2/library/heapq.html
# print("Should output [0, 1, 2, 3, 4, 5, 6, 7] -> ", kmergesort([4, 1, 5, 2, 6, 3, 7, 0], 3))
