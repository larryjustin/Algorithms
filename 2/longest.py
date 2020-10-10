def longest(a):
    height, maximum = search(a)
    return maximum


def search(b):
    if b == [] or b[0] == [] and b[2] == []:
        return 0, 0

    left_height, left_path = search(b[0])
    right_height, right_path = search(b[2])
#    print("left height = ", left_height, "  right height = ", right_height)
#    print("left   path = ", left_path, "  right   path = ", right_path)

    return max(left_height, right_height) + 1, max((left_height + right_height) + 2, left_path, right_path)


# print("\n[[], 1, []] = ", longest([[], 1, []]))
# print("\n[[[], 1, []], 2, [[], 3, []]] = ", longest([[[], 1, []], 2, [[], 3, []]]))
# print("\n[[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]] = ", longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
# print(longest(sort(random.sample(range(100), 100))))
