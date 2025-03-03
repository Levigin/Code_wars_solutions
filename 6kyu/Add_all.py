import heapq as hq


def add_all(lst):
    hq.heapify(lst)
    res = 0

    while len(lst) > 1:
        a = hq.heappop(lst)
        b = hq.heappop(lst)
        res += a + b
        hq.heappush(lst, a + b)
    return res


if __name__ == '__main__':
    nums_ = [1, 2, 3, 4]
    print(f'Ans: {add_all(nums_)}')
