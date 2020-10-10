import random


def qselect(i, a):
    if not a:
        return []
    pivot = random.choice(a)
    l = [x for x in a if x < pivot]            # less than
    e = [x for x in a if x == pivot]           # equal to
    g = [x for x in a if pivot < x]            # greater than
    if i <= len(l):                            # kth lies in l
        return qselect(i, l)
    elif i <= len(l) + len(e):                 # kth equal to pivot
        return pivot
    else:                                      # new selection
        j = i - len(l) - len(e)
        return qselect(j, g)


def find(a, i, k):
    if not a:
        return []
    delta = [abs(i - v) for v in a]
    difference = qselect(k, delta)
    kdelta = [y for y in delta if y <= difference][:k]
    result = []
    for vdelta in kdelta:
        result += [v for v in a if abs(v - i) == vdelta]
    if not result:
        return []
    else:
        return result[:k]


# print("returns [4,4]\t-> \t", find([4, 1, 3, 2, 7, 4], 5.2, 2))
# print("returns [4,7,4]\t-> \t", find([4, 1, 3, 2, 7, 4], 6.5, 3))
# print("returns [3,4]\t-> \t", find([5, 3, 4, 1, 6, 3], 3.5, 2))
