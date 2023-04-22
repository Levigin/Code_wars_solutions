from itertools import chain


# For hexagonal
def the_bee(n):
    dp = dict()
    lengths = [_ + n for _ in chain(range(n - 1), range(n - 1, -1, -1))]
    k = n
    res = []
    length = 2 * k - 1
    pinned_coordinates = []
    z = 0
    while z < (k - 1):
        res += [[x + k + z, x] for x in range(k - z - 1)]
        z += 1

    temp = []
    for item in res:
        y, x = item[0], item[1]
        temp.append([x, y])
    res += temp

    print(f'res: {res}')

    def recursive_seeker(y, x):
        # hexagonal check
        if [y, x] not in res:
            # base case
            if length - 1 in (y, x):
                return 1
            # recursion body
            # memo check
            if (y, x) not in dp.keys():
                dp[(y, x)] = recursive_seeker(y + 1, x) + recursive_seeker(y, x + 1) + recursive_seeker(y + 1, x + 1)
            return dp[(y, x)]
        else:
            return 0

    return recursive_seeker(0, 0)


print(the_bee(3))


def the_bee_(n: int):
    """bottom-up version"""
    length = 2 * n - 1
    print(f'length: {length}')
    # memoization:
    dp = [[0] * length for _ in range(length)]
    # restrictions:
    restricted_cells = set()
    for j in range(n - 1):
        for i in range(j, n - 1):
            restricted_cells.add((j, n + i))
            restricted_cells.add((n + i, j))
    # main cycle:
    for j in range(length):
        for i in range(length):
            if (j, i) not in restricted_cells:
                # base case:
                if 0 in [j, i]:
                    # print(f'zero for: {j=}, {i=}')
                    dp[j][i] = 1
                else:
                    # print(f'try to calc: {j=}, {i=}')
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1] + dp[j - 1][i - 1]
            else:
                dp[j][i] = 0
    return dp[length - 1][length - 1]


# For grid
# def robot(y_max: int, x_max: int):
#     # memoization
#     dp = {}
#
#     def recursive_seeker(y, x):
#         # base case
#         if y == y_max - 1 or x == x_max - 1:
#             return 1
#         # recursion body
#         # memo check
#         if (y, x) not in dp.keys():
#             dp[(y, x)] = recursive_seeker(y + 1, x) + recursive_seeker(y, x + 1)
#         return dp[(y, x)]
#
#     return recursive_seeker(0, 0)


# n = 3
# print([_ - 1 for _ in chain(range(1, n - 1), range(n - 1, 0, -1))])
# print([(i, j) for i, j in (range(3), range(1))])
