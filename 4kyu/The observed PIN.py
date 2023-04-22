from itertools import product

keyboard = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['', '0', '']]


def get_pins(observed: str):
    k = 0
    list_coordinates = []
    while k < len(observed):
        for i in range(len(keyboard)):
            for j in range(len(keyboard[0])):
                if keyboard[i][j] == observed[k]:
                    list_coordinates.append((i, j))
                    break
        k += 1

    all_neighs = []
    for y_, x_ in list_coordinates:
        all_neighs.append(get_neigh(y_, x_))

    return list(map(''.join, product(*all_neighs)))


def get_neigh(y: int, x: int):
    steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    neighs = ''
    for step in steps:
        new_y, new_x = y + step[0], x + step[1]
        if 0 <= new_y < len(keyboard) and 0 <= new_x < len(keyboard[0]) and keyboard[new_y][new_x] != '':
            neighs += keyboard[new_y][new_x]

    neighs += keyboard[y][x]
    return neighs


print(get_pins('11'))
