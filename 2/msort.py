
def merge(l, r, a):
    i = j = 0
    while i + j < len(a):
        if j == len(r) or (i < len(l) and l[i] < r[j]):
            a[i + j] = l[i]
            i += 1
        else:
            a[i + j] = r[j]
            j += 1


def mergesort(a):
    n = len(a)
    if n < 2:
        return a
    mid = n // 2
    l = a[0:mid]
    r = a[mid:n]
    mergesort(l)
    mergesort(r)
    merge(l, r, a)
    return a


# print(mergesort([4, 2, 5, 1, 6, 3]))

