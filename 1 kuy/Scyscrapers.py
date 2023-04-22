board_size: int
board_restrictions: list[list[int]]
board: list[list[int]]
vertical_restrictions: dict
horizontal_restrictions: dict
flag: bool


def solve_puzzle(clues):
    global board_size, board, board_restrictions, vertical_restrictions, horizontal_restrictions, flag
    board_size = len(clues) // 4

    board_restrictions = [[board_size] * board_size for _ in range(board_size)]
    board = [[0] * board_size for _ in range(board_size)]

    for i in range(board_size):
        curr_restrictions = find_restrictions(clues[i], clues[3 * board_size - i - 1])
        for j in range(board_size):
            if curr_restrictions[j] < board_restrictions[j][i]:
                board_restrictions[j][i] = curr_restrictions[j]

    for j in range(board_size):
        curr_restrictions = find_restrictions(clues[4 * board_size - j - 1], clues[board_size + j])
        for i in range(board_size):
            if curr_restrictions[i] < board_restrictions[j][i]:
                board_restrictions[j][i] = curr_restrictions[i]

    # backtracking

    vertical_restrictions = {key: set() for key in range(board_size)}
    horizontal_restrictions = {key: set() for key in range(board_size)}

    def backtracking(curr_j: int, curr_i: int):
        global vertical_restrictions, horizontal_restrictions, board, flag

        if curr_j == board_size:
            flag = False
            return

        for height in range(1, board_restrictions[curr_j][curr_i] + 1):
            if height not in vertical_restrictions[curr_i] and height not in horizontal_restrictions[curr_j]:
                if flag:
                    # do it:
                    vertical_restrictions[curr_i].add(height)
                    horizontal_restrictions[curr_j].add(height)
                    board[curr_j][curr_i] = height
                    # recurrent relations:
                    if curr_i == board_size - 1:
                        backtracking(curr_j + 1, 0)
                    else:
                        backtracking(curr_j, curr_i + 1)
                    # undo it
                    if flag:
                        vertical_restrictions[curr_i].remove(height)
                        horizontal_restrictions[curr_j].remove(height)
                        board[curr_j][curr_i] = 0

    flag = True
    backtracking(0, 0)

    return board


def find_restrictions(l_clue: int, r_clue: int) -> list[int]:
    global board_size
    res = [(board_size + 1 - l_clue + i) for i in range(l_clue - 1)] + [board_size] * (
            board_size + 2 - l_clue - r_clue) + [(board_size - i - 1) for i in range(r_clue - 1)]
    print(f'{res = }')
    if l_clue == 0:
        res = res[: -1]
    if r_clue == 0:
        res = res[1:]

    return res


print(solve_puzzle([7, 0, 0, 0, 2, 2, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 4]))

# def find_right_perms(l_clue: int, r_clue: int) -> list[list[int]]:
#     global board_size
#     permutations = []
#     restrictions = [(board_size + 1 - l_clue + i) for i in range(l_clue - 1)] + [board_size] * (
#                 board_size + 2 - l_clue - r_clue) + [(board_size - i - 1) for i in range(r_clue - 1)]
#
#     print(f'restrictions: {restrictions}')
#
#     def recursive_seeker(curr_permutation: list[int], rec_depth: int) -> None:  # , previous_element: int
#         # border case:
#         if rec_depth == board_size:
#             permutations.append(curr_permutation)
#             return
#
#         # body of rec:
#         for i in range(1, restrictions[rec_depth] + 1):
#             # recurrent relation:
#             if i not in curr_permutation:
#                 recursive_seeker(curr_permutation + [i], rec_depth + 1)
#
#     # rec call
#     recursive_seeker([], 0)
#
#     return permutations
