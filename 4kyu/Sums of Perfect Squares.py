def sum_of_squares(n):

    value = int(n ** 0.5)
    if value ** 2 == n:
        return 1
    i = 1
    while i * i <= n:
        value = int((n - (i ** 2)) ** 0.5)
        if value ** 2 == (n - i ** 2):
            return 2
        i += 1

    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    else:
        return 3


print(sum_of_squares(18))
