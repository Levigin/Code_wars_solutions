def land_perimeter(arr):
    per = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'X':
                per += 4 - get_len_neighs(arr, (i, j))

    return f"Total land perimeter: {per}"


def get_len_neighs(arrays: list, pos: tuple):
    dec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    length = 0
    for delta in dec:
        y_, x_ = pos[0] + delta[0], pos[1] + delta[1]
        if 0 <= y_ < len(arrays) and 0 <= x_ < len(arrays[0]) and arrays[y_][x_] == 'X':
            length += 1
    return length


board = ["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]
print(land_perimeter(board))
