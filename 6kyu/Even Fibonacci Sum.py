def even_fib(m):
    dict_fib = dict()
    res_list = []

    def fibonacci(n, res_list):
        if n in dict_fib:
            return dict_fib[n]

        if n in [0, 1]:
            return n

        dict_fib[n] = fibonacci(n - 1, res_list) + fibonacci(n - 2, res_list)
        if dict_fib[n] % 2 == 0:
            res_list.append(dict_fib[n])
        return dict_fib[n]

    fibonacci(m // 2, res_list)
    print(res_list)
    if len(res_list) == 0:
        return 0
    value = res_list[0]
    for i in range(1, len(res_list)):
        if value + res_list[i] <= m:
            value += res_list[i]
        else:
            return value
    return value

# print(even_fib(25997544))
