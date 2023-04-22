def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2 * n):
            x += i + j

    return x


def solve(n):  # don't pass the tests
    x = 0
    for i in range(n):
        x += i * 2 * n
    y = 0
    for i in range(2 * n):
        y += i * n
    # print(f'x = {x}, y = {y}')
    return x + y


def solve_update(n):
    return n ** 2 * ((n - 1) + (2 * n - 1))


# print(find_x(6))
print(solve(1))
print(solve_update(5))
print(solve(2))
print(solve(3))
print(solve(4))
print(solve(5))
print(solve(6))
