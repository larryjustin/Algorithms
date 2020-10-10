

def bsts(a):
    d = {0: 1}

    def f(d, a):
        if a not in d:
            count = 0
            for i in range(1, a + 1):
                count += f(d, i - 1) * f(d, a - i)
            d[a] = count
        return d[a]
    return f(d, a)


"""
print("bsts: Should return 2 -> ", bsts(2))
print("bsts: Should return 5 -> ", bsts(3))
print("bsts: Should return 42 -> ", bsts(5))
"""
