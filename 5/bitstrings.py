

def num_no(n):
    d = {0: 1, 1: 2}

    def f(d, n):
        if n not in d:
            d[n] = f(d, n - 1) + f(d, n - 2)
        return d[n]
    return f(d, n)


def num_yes(n):
    return pow(2, n) - num_no(n)


"""
print("num_no: Should return 5 -> ", num_no(3))
print("num_yes: Should return 3 -> ", num_yes(3))
"""
