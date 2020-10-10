import bisect


def find(a, i, k):
    if not a:
        return []
    pos = bisect.bisect(a, i)
    left, right = pos - 1, pos
    while k != 0:
        if right == len(a) or abs(i - a[left]) <= abs(a[right] - i):
            left -= 1
        elif left < 0 or abs(i - a[left]) > abs(a[right] - i):
            right += 1
        k -= 1

    return a[left + 1:right]


# print("returns [4,4] \t\t-> ", find([1, 2, 3, 4, 4, 7], 5.2, 2))
# print("returns [4,4,7] \t-> ", find([1, 2, 3, 4, 4, 7], 6.5, 3))
# print("returns [4,4,6] \t-> ", find([1, 2, 3, 4, 4, 6, 6], 5, 3))
# print("returns [2,3,4,4,5] -> ", find([1, 2, 3, 4, 4, 5, 6], 4, 5))
