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
