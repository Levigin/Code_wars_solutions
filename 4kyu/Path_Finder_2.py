steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def path_finder(maze):
    board = get_board(maze)
    counter = 1
    start = (0, 0)
    end = (len(board) - 1, len(board[0]) - 1)
    flag = False

    board[0][0] = counter
    front_wave = [start]
    while front_wave:
        new_front_wave = []
        counter += 1
        for neigh in get_neighs(front_wave, board):
            board[neigh[0]][neigh[1]] = counter
            if neigh not in new_front_wave:
                new_front_wave.append(neigh)

            if end in new_front_wave:
                flag = True
                # print('lala')
                break
        # print(f'new_front_wave: {new_front_wave}')
        front_wave = new_front_wave[:]
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         print(f'{board[i][j]} ', end='')
        #     print()
        # print()
        if flag:
            break

    if not flag:
        return False

    return board[-1][-1] - 1


def get_board(maze):
    maze = maze.split('\n')
    new_board = []
    for i in range(len(maze)):
        curr = []
        for j in range(len(maze[0])):
            if maze[i][j] == 'W':
                curr.append(maze[i][j])
            else:
                curr.append(0)
        new_board.append(curr)
    return new_board


def get_neighs(front: list[tuple], new_board):
    neighs = []
    for neigh in front:
        for delta in steps:
            new_y, new_x = neigh[0] + delta[0], neigh[1] + delta[1]
            if 0 <= new_y < len(new_board) and 0 <= new_x < len(new_board[0]) and \
                    new_board[new_y][new_x] != 'W' and 0 == new_board[new_y][new_x]:
                neighs.append((neigh[0] + delta[0], neigh[1] + delta[1]))
    return neighs


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])
d = '\n'.join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])
# print(d)
# print(get_board(d))
print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
