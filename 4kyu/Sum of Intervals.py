def sum_of_intervals(intervals):
    result = 0
    res = []
    interval = sorted(intervals)
    start, end = interval[0][0], interval[0][1]

    for i, intrvl in enumerate(interval[1:]):
        s, e = intrvl[0], intrvl[1]
        if s > end:
            res.append([start, end])
            start, end = s, e
        else:
            end = max(e, end)

    res.append([start, end])

    for i, j in res:
        result += j - i

    return result


# print(sum_of_intervals([(1, 20), (7, 10), (5, 8)]))
# print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
print(sum_of_intervals([(-328, -59), (-304, 322), (-128, 75), (-122, 18), (-86, 362), (-32, 253), (161, 177), (174, 425), (204, 364), (245, 425), (459, 477)]))
