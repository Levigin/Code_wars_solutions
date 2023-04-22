def max_sequence(arr: list):
    if sum(arr) < 0:
        return 0
    if len(arr) == 0:
        return 0

    result = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(curr_max + arr[i], arr[i])
        if result < curr_max:
            result = curr_max

    return result


def maxSequence(arr):
    max_, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max_:
            max_ = curr
    return max_


print(maxSequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
