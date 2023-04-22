import sys
sys.setrecursionlimit(100000)

directions = {'r': (0, 1),
              'l': (0, -1),
              'u': (-1, 0),
              'd': (1, 0)}


def path_counter(m):
    # grid building
    grid = []
    fy, fx = None, None

    for y_, row in enumerate(m.split('\n')):
        grid.append([])
        for x_, el in enumerate(row):
            if el == 'f':
                fy, fx = y_, x_
            grid[y_].append([el, False])

    Y, X = len(grid), len(grid[0])
    result = [[-1 for _ in range(X)] for _ in range(Y)]
    print(f'grid: {grid}')

    def rec(y: int, x: int, count: int):
        if not grid[y][x][1]:
            result[y][x] = count
            grid[y][x][1] = True
            for dyx in directions.values():
                dy, dx = (y + dyx[0]) % Y, (x + dyx[1]) % X
                if grid[dy][dx][0] != 'f' and directions[grid[dy][dx][0]] == (-dyx[0], -dyx[1]):
                    rec(dy, dx, count + 1)

    rec(fy, fx, 0)
    return result



test = """dfllllll
drrurrdu
rrlruldu
rrrrrrru"""

print(path_counter(test))
