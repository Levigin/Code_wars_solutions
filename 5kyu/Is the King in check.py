import numpy as np
from collections import defaultdict

list_figure = ['♟', '♔', '♛', '♝', '♞', '♜']


def king_is_in_check(chessboard: list):
    """ do your magic (; """

    new_chessboard = np.array(chessboard)
    Y, X = len(new_chessboard), len(new_chessboard)
    dict_position = defaultdict(lambda : [])
    # print(f'new_chessboard:\n {new_chessboard}')
    for i in range(len(chessboard)):
        for j in range(len(chessboard[0])):
            if chessboard[i][j] in list_figure:
                dict_position[chessboard[i][j]].append((i, j))

    print(f'dict_pos: {dict_position}')
    if '♔' not in dict_position:
        return False

    knights_move = [(-2, 1), (2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    flag = False

    # print(new_chessboard.diagonal(abs(dict_position['♝'][0] - dict_position['♝'][1])))
    # print(new_chessboard[:, ::-1].diagonal(X - 1 - (dict_position['♝'][0] + dict_position['♝'][1])))

    for figure, value in dict_position.items():
        if figure == '♔':
            pass
        elif figure == '♛':
            for item in range(len(value)):
                dy, dx = dict_position[figure][item][0], dict_position[figure][item][1]
                check = check_queen(new_chessboard, (dy, dx), (dict_position['♔'][0][0], dict_position['♔'][0][1]), figure)
                if check:
                    return True
        elif figure == '♝':
            for item in range(len(value)):
                dy, dx = dict_position[figure][item][0], dict_position[figure][item][1]
                check = check_bishop(new_chessboard, (dy, dx), (dict_position['♔'][0][0], dict_position['♔'][0][1]), figure)
                if check:
                    return True
        elif figure == '♞':
            for item in range(len(value)):
                for move in knights_move:
                    y_, x_ = dict_position[figure][item][0] + move[0], dict_position[figure][item][1] + move[1]
                    if 0 <= y_ < Y and 0 <= x_ < X and \
                            (y_, x_) == (dict_position['♔'][0][0], dict_position['♔'][0][1]):
                        flag = True
                if flag:
                    return True
        elif figure == '♜':
            for item in range(len(value)):
                dy, dx = dict_position[figure][item][0], dict_position[figure][item][1]
                check = check_rook(new_chessboard, (dy, dx), (dict_position['♔'][0][0], dict_position['♔'][0][1]))
                if check:
                    return True
        elif figure == '♟':
            for item in range(len(value)):
                dy, dx = dict_position[figure][item][0], dict_position[figure][item][1]
                if (dy + 1, dx + 1) == (dict_position['♔'][0][0], dict_position['♔'][0][1]) or \
                        (dy + 1, dx - 1) == (dict_position['♔'][0][0], dict_position['♔'][0][1]):
                    return True

    return False


def check_queen(chessboard: list, pos_queen: tuple, pos_king: tuple, figure: str):
    if check_bishop(chessboard, pos_queen, pos_king, figure) or check_rook(chessboard, pos_queen, pos_king):
        return True
    return False


def check_bishop(chessboard: list, pos_bishop: tuple, pos_king: tuple, figure: str):
    dy, dx = pos_bishop[0], pos_bishop[1]
    # print(f"dy: {dy}, dx: {dx}")
    diag1 = list(chessboard.diagonal(abs(dy - dx) if dx > dy else -abs(dy - dx)))
    diag2 = list(chessboard[:, ::-1].diagonal(len(chessboard) - 1 - (dy + dx)))
    check_list_fig = []
    if '♔' in diag1:
        ind_fig = diag1.index(figure)
        ind_king = diag1.index('♔')
        if ind_king > ind_fig:
            check_list_fig = diag1[ind_fig + 1: ind_king]
        else:
            check_list_fig = diag1[ind_king + 1: ind_fig]
    elif '♔' in diag2:
        ind_fig = diag2.index(figure)
        ind_king = diag2.index('♔')
        if ind_king > ind_fig:
            check_list_fig = diag2[ind_fig + 1: ind_king]
        else:
            check_list_fig = diag2[ind_king + 1: ind_fig]
    else:
        return False

    for i in list_figure:
        if i in check_list_fig:
            return False

    return True


def check_rook(chessboard: list, pos_rook: tuple, pos_king: tuple):
    dy, dx = pos_rook[0], pos_rook[1]

    print(f'x: {chessboard[dy, :]}')
    # print(f'y: {chessboard[:, dx]}')
    # for x coordinates
    if '♔' in chessboard[dy, :]:
        if pos_king[1] < pos_rook[1]:
            check_list_figure = chessboard[dy, pos_king[1] + 1:pos_rook[1]]
        else:
            check_list_figure = chessboard[dy, pos_rook[1] + 1:pos_king[1]]
    # for y coordinates
    elif '♔' in chessboard[:, dx]:
        if pos_king[0] < pos_rook[0]:
            check_list_figure = chessboard[pos_king[0] + 1:pos_rook[0], dx]
        else:
            check_list_figure = chessboard[pos_rook[0] + 1:pos_king[0], dx]
    else:
        return False
    print(f'check_list_figure: {check_list_figure}')
    #
    for i in list_figure:
        if i in check_list_figure:
            return False

    return True


board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '♟', ' ', ' ', ' ', ' '],
    [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
board1 = [[' ', '♛', ' ', ' ', ' ', ' ', '♔', ' '],
          [' ', ' ', ' ', '♛', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

print(king_is_in_check(board1))
