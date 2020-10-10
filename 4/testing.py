import heapq
import timeit


def test1():
    a = list(range(1000000))
    random.shuffle(a)
    heapq.heapify(a)


def test2():
    a = list(range(1000000))
    random.shuffle(a)
    heap = []
    for x in a:
        heapq.heappush(heap, x)


print(timeit.timeit("test1", globals=globals()))
print(timeit.timeit("test2", globals=globals()))


# time start
# time end
# start - end
