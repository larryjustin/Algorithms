import bisect


def sort(a):
    if not a:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]


def sorted(a2):
    results = []
    for rec in a2:
        if isinstance(rec, list):
            results.extend(rec)
            results = sorted(results)
        else:
            results.append(rec)
    return results


def insert(t, x):
    st = sorted(t)
    if search(st, x):
        return st
    else:
        bisect.insort(st, x)
        return sort(st)


def search(nl, target):
    for thing in nl:
        if type(thing) is list:
            if search(thing, target):
                return True
        if thing == target:
            return True
    return False


def _search(a, value):
    if len(a) == 3:
        if value == a[1]:
            print(a)
        elif value < a[1]:
            _search(a[0], value)
        else:
            _search(a[2], value)
    elif len(a) != 3:
        print([])
