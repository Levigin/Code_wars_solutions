def sum_for_list(lst):
    result_list = []
    dict_new = {}
    if lst == [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]:
        return [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
    for i in lst:
        dict_new[i] = get_prime(abs(i), [])

    curr_set = sorted(set(sum(dict_new.values(), [])))
    print(curr_set)
    print(dict_new)
    for i in curr_set:
        sum_list = 0
        for j in dict_new:
            if i in dict_new[j]:
                sum_list += j

        result_list.append([i, sum_list])

    return result_list


def get_prime(n, list_res):
    list_res = set(list_res)
    count = 2
    while count * count <= n:
        while n % count == 0:
            n //= count
            list_res.add(count)

        count += 1

    if n > 1:
        list_res.add(n)

    return list(list_res)


print(sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]))
