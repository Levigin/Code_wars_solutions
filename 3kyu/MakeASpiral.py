import sys
sys.setrecursionlimit(12000)


def spiralize(size):
    res = []

    for g in range(size):
        temp = []
        for j in range(size):
            temp.append(None)
        res.append(temp)

    p = size * 4
    val = 1

    def rec(y, x, count, delta, perimeter, v, result):

        if count == perimeter - 4:
            delta += 1
            perimeter += (size - 2 * delta) * 4 - 4
            if delta % 2 == 0:
                v = 1
            else:
                v = 0

        if count == size ** 2:
            result[y][x] = v
            return result

        result[y][x] = v
        if y == 0 + delta and x < size - 1 - delta:
            rec(y, x + 1, count + 1, delta, perimeter, v, result)
        elif x == size - 1 - delta and y < size - 1 - delta:
            rec(y + 1, x, count + 1, delta, perimeter, v, result)
        elif y == size - 1 - delta and x > 0 + delta:
            rec(y, x - 1, count + 1, delta, perimeter, v, result)
        elif x == 0 + delta and y >= 0 + delta:
            rec(y - 1, x, count + 1, delta, perimeter, v, result)

    rec(0, 0, 1, 0, p, val, res)

    return res


c = spiralize(100)

for i in c:
    print(i)

a = [[1, 1, 1, 1, 1],
     [0, 0, 0, 0, 1],
     [1, 1, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]]  # 5

b = [[1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 0, 1],
     [1, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1]]  # 6

c = [[1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1]]  # 7

d = [[1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1]]  # 8

