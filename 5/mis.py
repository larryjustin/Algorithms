
def max_wis(a):
    d = {}

    def i(d, a):
        l = len(a)
        if not a or max(a) < 0:
            d[l] = (0, [])
        else:
            if l not in d:
                f1 = i(d, a[:-1])
                f2 = i(d, a[:-2])
                f2 = (f2[0] + a[l - 1], f2[1] + [a[l - 1]])
                d[l] = f1 if f1[0] >= f2[0] else f2
        return d[l]
    return i(d, a)


def max_wis2(a):
    if not a or max(a) < 0:
        return 0, []
    x, y = (0, []), (0, [])
    for i in range(0, len(a)):
        temp = x
        if x[0] < y[0] + a[i]:
            n = list(y[1])
            n.append(a[i])
            x = (y[0] + a[i], n)
        y = temp
    return x


"""
print("MW1: Should return (12, [7, 5]) -> ", max_wis([7, 8, 5]))
print("MW1: Should return (10, [10]) -> ", max_wis([-1, 8, 10]))
print("MW1: Should return (0, []) -> ", max_wis([]))
print("MW1: Should return (0, []) -> ", max_wis([-5, -1, -4]), "\n")

print("MW2: Should return (12, [7, 5]) -> ", max_wis2([7, 8, 5]))
print("MW2: Should return (10, [10]) -> ", max_wis2([-1, 8, 10]))
print("MW2: Should return (0, []) -> ", max_wis2([]))
print("MW2: Should return (0, []) -> ", max_wis2([-5, -1, -4]), "\n")
"""
