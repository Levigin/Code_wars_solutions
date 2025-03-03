import math


def closest(strng):
    array_num = strng.strip().split(' ')
    # print(f'array_num: {array_num}')
    refactor_nums = []
    for ind, num in enumerate(array_num):
        tmp_num = sum(map(int, (list(num))))
        refactor_nums.append([tmp_num, ind])

    new_array = sorted(refactor_nums, key=lambda x: x[0])

    # print(f'refactor_num: {refactor_nums}')
    # print(f'new_array: {new_array}')
    min_closest = math.inf
    res = []
    for i in range(len(new_array) - 1):
        if min_closest > (c := (new_array[i + 1][0] - new_array[i][0])):
            min_closest = c
            res = [[new_array[i][0], new_array[i][1], int(array_num[new_array[i][1]])],
                   [new_array[i +1][0], new_array[i + 1][1], int(array_num[new_array[i + 1][1]])]]

    return res


# print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))
# print(closest("444 2000 445 544"))
print(closest(""))
# print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"))
