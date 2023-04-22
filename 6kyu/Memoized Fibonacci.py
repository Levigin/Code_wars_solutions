list_fib = dict()


def fibonacci(n):
    if n in list_fib:
        return list_fib[n]

    if n in [0, 1]:
        return n

    list_fib[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return list_fib[n]


print(fibonacci(70))
