def permutations(s):

    result = []

    def rec(s, sub_s):

        if len(s) == len(sub_s):
            result.append(list(sub_s))
            return

        for i in range(len(s)):
            if i not in sub_s:
                sub_s.append(i)
                rec(s, sub_s)
                sub_s.remove(i)

    rec(s, [])
    res = get_convert(result, s)

    return list(set(res))


def get_convert(list_of_list, nums):
    res = []
    array = []
    for i in range(len(list_of_list)):
        temp = []
        for j in list_of_list[i]:
            temp.append(nums[j])

        res.append(temp)

    for i in res:
        array.append(''.join(i))

    return array


print(permutations('aabb'))

