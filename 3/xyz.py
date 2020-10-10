

def find(a):
    a.sort()
    array = []
    for pos in range(len(a)):
        left, right = 0, len(a) - 1

        while left < right:
            if left == pos:
                left += 1
            elif right == pos:
                right -= 1
            elif a[left] + a[right] == a[pos]:
                array.append((a[left], a[right], a[pos]))
                left += 1
                right -= 1
            elif a[left] + a[right] > a[pos]:
                right -= 1
            elif a[left] + a[right] < a[pos]:
                left += 1
    return array


# print("returns [(1,3,4), (1,2,3), (1,4,5), (2,3,5)] -> ", find([1, 4, 2, 3, 5]))

