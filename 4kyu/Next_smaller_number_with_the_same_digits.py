def next_smaller(n):
    perm = list(map(lambda x: int(''.join(x)), list(str(n))))
    ind = len(perm) - 1
    if len(perm) < 2:
        return -1
    if sorted(perm) == perm:
        return -1

    while ind > 0:
        if perm[ind - 1] > perm[ind]:
            temp = perm[ind - 1:]
            remains = perm[:ind - 1]
            count = 0
            for j, item in enumerate(temp[1:], start=1):
                next_small = -1
                if temp[0] > item > next_small:
                    count = j
            temp[0], temp[count] = temp[count], temp[0]
            result = list(map(str, remains + [temp[0]] + list(sorted(temp[1:], reverse=True))))
            print(f'{len(perm) = }, {result = }')
            if len(result) != len(perm) or result[0] == '0':
                return -1
            return int(''.join(result))
        ind -= 1


print(next_smaller(1027))

