def count_Kprimes(k, start, nd):
    result = []

    for i in range(start, nd + 1):
        count = 2
        list_count = []
        curr_i = i
        while count * count <= curr_i:
            while curr_i % count == 0:
                curr_i //= count
                list_count.append(count)
            count += 1

        if curr_i > 1:
            list_count.append(curr_i)
        if len(list_count) == k:
            result.append(i)

    return result


def puzzle(s):
    count = 0
    one_primes = count_Kprimes(1, 1, s)
    three_primes = count_Kprimes(3, 7, s)
    seven_primes = count_Kprimes(7, 127, s)
    for i in one_primes:
        for j in three_primes:
            for k in seven_primes:
                if i + j + k == s:
                    print(f'i = {i}, j = {j}, k = {k}')
                    count += 1

    return count


print(puzzle(143))