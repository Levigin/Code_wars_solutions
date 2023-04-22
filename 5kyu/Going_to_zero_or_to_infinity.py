
def going(n):
    res2 = 0
    curr_res = 1
    for i in range(1, n + 1):
        curr_res *= i
        res2 += curr_res

    return int(res2 / curr_res * 1000000) / 1000000


print(going(200))
