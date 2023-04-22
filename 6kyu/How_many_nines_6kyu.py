
def count_round_range(k):
    if k == 0:
        return 0
    else:
        print('count_round_range(k - 1)')
        return 10 ** (k - 1) + 9 * count_round_range(k - 1)


def count_number5(n):
    if n < 10:
        if n >= 9:
            return 1
        else:
            return 0

    s = str(n)
    digits = len(s)
    hi_digit, lo_n = int(s[0]), int(s[1:])  # разделяем число на первую цифру и остальные (1000 => 1 и 000 -> 0)
    if hi_digit < 9:
        return hi_digit * count_round_range(digits - 1) + count_number5(lo_n)
    elif hi_digit == 9:
        return hi_digit * count_round_range(digits - 1) + lo_n + 1
    elif hi_digit > 9:
        return (hi_digit - 1) * count_round_range(digits - 1) + 10 ** (digits - 1) + count_number5(lo_n)


print(count_number5(1000))