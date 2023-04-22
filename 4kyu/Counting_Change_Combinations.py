def count_change(money, coins):
    all_perm = []

    def rec(m, list_, curr_sum, index):
        if curr_sum == m:
            all_perm.append(list_)

        for i in range(index, len(coins)):
            if (new_curr_sum := curr_sum + coins[i]) <= m:
                new_list = list_ + [new_curr_sum]
                print(f'new_curr_sum: {new_curr_sum}')
                print(f'new_list: {new_list}')
                rec(m, new_list, new_curr_sum, i)

    rec(money, [], 0, 0)
    return len(all_perm)


def count_change_(money, coins):
    if money == 0:
        return 1
    data = [0] * (money + 1)
    data[0] = 1
    for c in coins:
        for i in range(1, money + 1):
            if i >= c:
                data[i] += data[i - c]
    return data[money]


print(count_change(0, [1, 2]))