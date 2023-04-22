from collections import defaultdict


def subsequence_sums(arr: list, s: int):
    # TODO - your code here
    prev = defaultdict(lambda: 0)
    result = 0
    curr_sum = 0
    for i in arr:
        curr_sum += i
        if curr_sum == s:
            result += 1
        if (curr_sum - s) in prev:
            result += prev[curr_sum - s]
        prev[curr_sum] += 1

    return result


print(subsequence_sums([1, 5, -2, 4, 0, -7, -3, 6], 4))  # 4
# print(subsequence_sums([9, -2, -5, 8, 6, -10, 0, -4], -1))  # 2
