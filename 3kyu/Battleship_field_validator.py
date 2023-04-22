from collections import deque

SHIPS = {1: 4, 2: 3, 3: 2, 4: 1}


def validate_battlefield(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                list_ships = get_deq_neighs(field, [i, j])
                print(f'{list_ships = }')
                if list_ships:
                    for block in list_ships:
                        field[block[0]][block[1]] = 0
                else:
                    return False

    for i in SHIPS.values():
        if i != 0:
            return False
    return True


def check_submarines(grid: list[list], pos: list):
    diagonal_steps = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    for step in diagonal_steps:
        y_, x_ = step[0] + pos[0], step[1] + pos[1]
        if 0 <= y_ < len(grid) and 0 <= x_ < len(grid[0]) and grid[y_][x_] == 1:
            return False
    return True


def get_deq_neighs(grid: list[list], pos: list):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighs = deque()
    all_neighs = []
    neighs.append(pos)
    while neighs:
        # print(f'{neighs = }')
        all_neighs.append(neighs[0])
        curr_ship = neighs.pop()
        # checking the component part of the ship:
        if check_submarines(grid, curr_ship):
            for step in delta:
                y_, x_ = step[0] + curr_ship[0], step[1] + curr_ship[1]
                if 0 <= y_ < len(grid) and 0 <= x_ < len(grid[0]) and grid[y_][x_] == 1 and [y_, x_] not in all_neighs:
                    neighs.append([y_, x_])
            if len(neighs) > 1:
                return False
        else:
            return False

    if len(all_neighs) > 4:
        return False
    SHIPS[len(all_neighs)] -= 1
    print(f'{SHIPS[len(all_neighs)] = }, {len(all_neighs) = }, {SHIPS = }')
    if SHIPS[len(all_neighs)] < 0:
        return False

    return all_neighs


battleField = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]]
# battleField1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))
