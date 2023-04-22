def is_solved(board):
    return check_the_field(board)


def check_the_field(tic_tac_toe_field):
    res_row = []
    res_col = []
    res_diagonal = []
    res_diagonal1 = []

    l = len(tic_tac_toe_field)

    for i in range(len(tic_tac_toe_field)):
        temp = []
        for j in range(len(tic_tac_toe_field)):
            temp.append(tic_tac_toe_field[j][i])
        res_col.append(temp)
        res_row.append(tic_tac_toe_field[i])
        res_diagonal.append(tic_tac_toe_field[i][i])
        res_diagonal1.append(tic_tac_toe_field[l - i - 1][i])

    res_diagonal_bool = all(x == res_diagonal[0] for x in res_diagonal) and all(x != 0 for x in res_diagonal)
    res_diagonal1_bool = all(x == res_diagonal1[0] for x in res_diagonal1) and all(x != 0 for x in res_diagonal1)

    if res_diagonal_bool or res_diagonal1_bool:
        if res_diagonal[0] == 1 or res_diagonal1[0] == 1:
            return 1
        if res_diagonal[0] == 2 or res_diagonal1[0] == 2:
            return 2

    for i in res_row:
        if all(x == i[0] for x in i) and all(x != " " for x in i) and i[0] == 1:
            return 1
        if all(x == i[0] for x in i) and all(x != " " for x in i) and i[0] == 2:
            return 2
    for i in res_col:
        if all(x == i[0] for x in i) and all(x != " " for x in i) and i[0] == 1:
            return 1
        if all(x == i[0] for x in i) and all(x != " " for x in i) and i[0] == 2:
            return 2

    for i in range(len(tic_tac_toe_field)):
        for j in range(len(tic_tac_toe_field)):
            if tic_tac_toe_field[i][j] == 0:
                return -1

    return 0


board = [[0, 1, 1],
         [2, 0, 2],
         [2, 1, 0]]
print(is_solved(board))