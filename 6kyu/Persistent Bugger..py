def persistence(n):

    if n < 10:
        return 0
    counter = 0
    curr_n = n
    while True:

        if curr_n < 10:
            curr_n = curr_n
            break
        curr_n = support_method(curr_n)
        counter += 1

    return counter


def support_method(n: int) -> int:
    list_digit = list(str(n))
    multiply = 1
    for i in list_digit:
        multiply *= int(i)

    return multiply


print(persistence(999))