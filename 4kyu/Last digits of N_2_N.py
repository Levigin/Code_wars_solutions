import time


def green_no_optimization(n):
    j = 2
    i = 1
    step = 1

    if n == 1:
        return 1

    flag = True
    while flag:
        if (j ** 2) % (10 ** len(str(j))) == j:
            i += 1
            if i == n:
                return j
            else:
                j += 1
        else:
            j += 1

    return j


def green_so_so(n):
    res_five = 5
    res_six = 6
    step = 10

    if n == 1:
        return 1
    elif n == 2:
        return 5
    elif n == 3:
        return 6

    count = 3
    while count < n:
        # for five
        for i in range(1, 10):
            curr_num_f = step * i + res_five
            curr_num_s = step * i + res_six
            if (curr_num_f ** 2) % (10 ** len(str(curr_num_f))) == curr_num_f:
                res_five = curr_num_f
                count += 1
                if count == n:
                    return res_five
            elif (curr_num_s ** 2) % (10 ** len(str(curr_num_s))) == curr_num_s:
                res_six = curr_num_s
                count += 1
                if count == n:
                    return res_six

        step *= 10


def green(n):
    set_value = set()

    num1 = 5
    num2 = 6
    set_value |= {num1, num2}
    counter = 2
    step = 2

    while counter < n + n // 5:
        power_of_ten = 10 ** step
        num1 = num1 ** 2 % power_of_ten
        num2 = power_of_ten + 1 - num1
        set_value |= {num1, num2}
        counter += 2
        step += 1

    set_value = list(sorted(set_value))
    set_value = [1] + set_value

    return set_value[n - 1]


start = time.time_ns()
print(green(5))
end = time.time_ns()
print(f'time elapsed: {(end - start) // 10 ** 6} milliseconds')


# print(green_so_so(7))
# print(green_so_so(8))
# print(green_so_so(9))
# print(green_so_so(10))
# print(green_so_so(11))
# print(green_so_so(12))
# start = time.time_ns()
# print(green_so_so(5000))
# end = time.time_ns()
# print(f'time = {(end - start) // 10 ** 6} millisec ')
