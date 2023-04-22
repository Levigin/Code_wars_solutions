def next_smaller(n):
    list_digit = list(str(n))
    i = len(list_digit) - 1
    while i > 0:
        if list_digit[i] != '0' or i - 1 != 0:
            if int(list_digit[i]) < int(list_digit[i - 1]):
                i -= 1
                break

        i -= 1

        if i == 0:
            return -1

    remain = list_digit[i:]
    result = []

    def rec(array, sub_remain):

        if len(sub_remain) == len(array):
            result.append(list(sub_remain))
            return

        for j in range(len(array)):
            if j not in sub_remain:
                sub_remain.append(j)
                rec(array, sub_remain)
                sub_remain.remove(j)

    rec(remain, [])

    res = get_convert(result, remain)
    try:
        x = max(get_convert_to_int(res, int(''.join(remain))))
    except:
        return -1

    list_digit[i:] = list(str(x))

    return int(''.join(list_digit))


def get_convert(list_of_list, nums):
    res = []

    for i in range(len(list_of_list)):
        temp = []
        for j in list_of_list[i]:
            temp.append(nums[j])

        res.append(temp)

    return res


def get_convert_to_int(list_of_list, n):

    res = []
    nums = []
    for i in range(len(list_of_list)):
        res.append(''.join(list_of_list[i]))

    # for i in res:
    #     if i < n:
    #         nums.append(i)

    return res


print(next_smaller(1207))