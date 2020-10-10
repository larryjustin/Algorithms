def mergesort(a, count):
    n = len(a)
    if n < 2:
        return 0
    else:
        mid = n // 2
        l = a[0:mid]
        r = a[mid:n]

        count += mergesort(l, count) + mergesort(r, count)

        i = j = 0
        while i + j < len(a):
            if j == len(r) or (i < len(l) and l[i] < r[j]):
                a[i + j] = l[i]
                i += 1
                count += (len(l) - j)
            else:
                a[i + j] = r[j]
                j += 1
    return count


def num_inversions(a):
    return mergesort(a, 0)


# print("(CA=4) Number of Inversions: ", num_inversions([4, 1, 3, 2]))
# print("(CA=3) Number of Inversions: ", num_inversions([2, 4, 1, 3]))
