def int_cube_sum_div(n):
    counter = n
    val = 1
    res = None
    while counter >= 0:
        if val ** 3 % get_sum_divisors(val) == 0:
            res = val
            counter -= 1
        val += 1
    return res


def get_sum_divisors(num: int):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num//i)

    return sum(res)


print(int_cube_sum_div(5))
