def prime_bef_aft(num):
    num_left = num
    num_right = num
    flag = True
    if num <= 4:
        return [3, 5]
    while flag:
        num_left -= 1
        for i in range(2, int(num_left ** 0.5) + 1):
            if num_left % i == 0:
                flag = True
                break
            flag = False

    flag = True

    while flag:
        num_right += 1
        for i in range(2, int(num_right ** 0.5) + 1):
            if num_right % i == 0:
                flag = True
                break
            flag = False

    return [num_left, num_right]


print(prime_bef_aft(3))