def sudoku(puzzle):
    rec_sudoku(puzzle)
    return puzzle


def rec_sudoku(puzzle):
    indexes = find_null_element(puzzle)
    print(indexes)
    if indexes is None:
        return True
    list_possible_numbers = possible_values(puzzle, indexes)
    print(f"list_possible_numbers = {list_possible_numbers}")
    for i in list_possible_numbers:
        if not is_valid(puzzle, indexes):
            puzzle[indexes[0]][indexes[1]] = i
            if rec_sudoku(puzzle):
                return True
            puzzle[indexes[0]][indexes[1]] = 0
    return False


def is_valid(board, pos):
    if check_row(board, pos) and check_col(board, pos) and (
            set(check_squared(board, pos)) == len(check_squared(board, pos))):
        return True
    return False


def check_row(board: list, pos: tuple):
    row_list = [i for i in board[pos[0]]]
    # Check
    if len(row_list) == len(set(row_list)):
        return True
    return False


def check_col(board: list, pos: tuple):
    col_list = [i[pos[1]] for i in board]

    if len(col_list) == len(set(col_list)):
        return True
    return False


def check_squared(board: list, pos: tuple):
    # Квадраты идут по слева направо сверху вниз, 1 элемент кортежа отвечает за строку, 2 за столбцы
    first_sq = [(0, 3), (0, 3)]
    second_sq = [(0, 3), (3, 6)]
    third_sq = [(0, 3), (6, 9)]
    fourth_sq = [(3, 6), (0, 3)]
    fifth_sq = [(3, 6), (3, 6)]
    sixth_sq = [(3, 6), (6, 9)]
    seventh_sq = [(6, 9), (0, 3)]
    eighth_sq = [(6, 9), (3, 6)]
    ninth_sq = [(6, 9), (6, 9)]

    if (0 <= pos[0] < 3) and (0 <= pos[1] < 3):
        select_number = first_sq

    elif (0 <= pos[0] < 3) and (3 <= pos[1] < 6):
        select_number = second_sq

    elif (0 <= pos[0] < 3) and (6 <= pos[1] < 9):
        select_number = third_sq

    elif (3 <= pos[0] < 6) and (0 <= pos[1] < 3):
        select_number = fourth_sq

    elif (3 <= pos[0] < 6) and (3 <= pos[1] < 6):
        select_number = fifth_sq

    elif (3 <= pos[0] < 6) and (6 <= pos[1] < 9):
        select_number = sixth_sq

    elif (6 <= pos[0] < 9) and (0 <= pos[1] < 3):
        select_number = seventh_sq

    elif (6 <= pos[0] < 9) and (3 <= pos[1] < 6):
        select_number = eighth_sq

    elif (6 <= pos[0] < 9) and (6 <= pos[1] < 9):
        select_number = ninth_sq

    squared = []
    for i in range(select_number[0][0], select_number[0][1]):
        squared += board[i][select_number[1][0]:select_number[1][1]]

    return squared


def find_null_element(board: list):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def possible_values(board: list, pos: tuple):
    possible_num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    row_list = set([i for i in board[pos[0]]])
    col_list = set([i[pos[1]] for i in board])
    sq = set(check_squared(board, pos))
    # print(f'row_list = {row_list}, col_list = {col_list}, sq = {sq}')
    possible_num -= row_list
    possible_num -= col_list
    possible_num -= sq
    for i in possible_num:
        if i == 0:
            possible_num.remove(0)

    return list(possible_num)


def print_board(board):
    for i in board:
        print(i)


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# print(check_col(solution, (0, 2)))
# print(check_squared(solution, (3, 2)))
# print(find_null_element(solution))
# print(possible_values(solution, (1, 2)))
print(sudoku(puzzle))
print_board(puzzle)
