import math


def zeros(n):
    if n == 0:
        return 0
    k = int(math.log(n, 5))
    count = 0
    for i in range(1, k + 1):

       count += n // 5**i

    return count



print(zeros(12))