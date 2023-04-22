import math


def find_reverse_number(n: int) -> int:
    l = math.floor((math.log10(n)))
    flag = 1 < n < 1.1 * (10 ** l)
    p = 10 ** (l - (1 if flag else 0))
    n -= p
    list1 = list(str(n // (10 if n >= p else 1)))
    list1.reverse()
    return n * (10 ** (l - (1 if flag else 0))) + int("".join(list1))



print(find_reverse_number(100))