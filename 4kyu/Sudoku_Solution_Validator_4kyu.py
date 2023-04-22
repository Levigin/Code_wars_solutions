def valid_solution(board):

    def valid_all(col_or_row: list):
        list_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return sorted(col_or_row) == list_digit

    def valid_rows(curr_board):
        for i in board:
            if not valid_all(i):
                return False
        return True

    def valid_col(curr_board):

        for i in range(len(curr_board)):
            temp_list = []
            for j in range(len(curr_board[0])):
                temp_list.append(board[j][i])
            if not valid_all(temp_list):
                return False
        return True

    def valid_square(curr_board):
        list_square = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                list_square = curr_board[i][j:j+3] + curr_board[i+1][j:j+3] + curr_board[i+2][j:j+3]

                if not valid_all(list_square):
                    return False

        return True

    if valid_square(board) == True and valid_col(board) == True and valid_rows(board) == True:
        return True
    else:
        return False


sudoku =   [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

sudoku1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
           [4, 9, 8, 2, 6, 1, 3, 7, 5],
           [7, 5, 6, 3, 8, 4, 2, 1, 9],
           [6, 4, 3, 1, 5, 8, 7, 9, 2],
           [5, 2, 1, 7, 9, 3, 8, 4, 6],
           [9, 8, 7, 4, 2, 6, 5, 3, 1],
           [2, 1, 4, 9, 3, 5, 6, 8, 7],
           [3, 6, 5, 8, 1, 7, 9, 2, 4],
           [8, 7, 9, 6, 4, 2, 1, 3, 5]]

print(valid_solution(sudoku1))
