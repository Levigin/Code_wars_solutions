class Zombie:

    def __init__(self, step: int, row: int, hp: int, col: int = None):
        self.step = step
        self.row = row
        self.col = col
        self.hp = hp

    def step_up(self, other: 'GameBoard'):
        self.col -= 1
        other.game_board[self.row][self.col] = self
        other.game_board[self.row][self.col + 1] = ' '

    def step_on_board(self, other: 'GameBoard'):
        self.col = len(other.game_board[0]) - 1
        other.game_board[self.row][self.col] = self

    def get_damage(self, damage: int):
        self.hp -= damage

    def __str__(self):
        return f'Z: {self.hp}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.row, self.col, self.hp))


class Plant:
    def __init__(self, damage: int, row: int, col: int):
        self.damage = damage
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f'{self.damage}'

    def __repr__(self):
        return str(self)

    def shoot(self, other: 'GameBoard'):
        damage = 0
        curr_col = self.col
        while curr_col < len(other.game_board[0]):
            if isinstance(other.game_board[self.row][curr_col], Zombie):
                temp = other.game_board[self.row][curr_col].hp
                if damage != 0:
                    other.game_board[self.row][curr_col].get_damage(damage)
                    if (c := other.game_board[self.row][curr_col].hp) < 0:
                        damage += damage - temp
                        other.zombie_die.append(other.game_board[self.row][curr_col])
                        other.game_board[self.row][curr_col] = ' '
                    elif other.game_board[self.row][curr_col].hp == 0:
                        other.zombie_die.append(other.game_board[self.row][curr_col])
                        other.game_board[self.row][curr_col] = ' '
                        damage = 0
                        break
                    else:
                        damage = 0
                        break
                else:
                    other.game_board[self.row][curr_col].get_damage(self.damage)
                    if (c := other.game_board[self.row][curr_col].hp) < 0:
                        damage += self.damage - temp
                        other.zombie_die.append(other.game_board[self.row][curr_col])
                        other.game_board[self.row][curr_col] = ' '
                    elif other.game_board[self.row][curr_col].hp == 0:
                        other.zombie_die.append(other.game_board[self.row][curr_col])
                        other.game_board[self.row][curr_col] = ' '
                        break
                    else:
                        break
            curr_col += 1

    def get_coordinate(self):
        return self.row, self.col


class PlantS(Plant):
    def __init__(self, damage: int, row: int, col: int):
        super().__init__(damage, row, col)

    def shoot_diagonal_top(self, other: 'GameBoard'):
        y, x = self.row, self.col

        while y >= 0 and x < len(other.game_board[0]):
            if isinstance(other.game_board[y][x], Zombie):
                other.game_board[y][x].get_damage(self.damage)
                if other.game_board[y][x].hp == 0:
                    other.zombie_die.append(other.game_board[y][x])
                    other.game_board[y][x] = ' '
                break
            y -= 1
            x += 1

    def shoot_diagonal_down(self, other: 'GameBoard'):
        y, x = self.row, self.col

        while y < len(other.game_board) and x < len(other.game_board[0]):
            if isinstance(other.game_board[y][x], Zombie):
                other.game_board[y][x].get_damage(self.damage)
                if other.game_board[y][x].hp == 0:
                    other.zombie_die.append(other.game_board[y][x])
                    other.game_board[y][x] = ' '
                break
            y += 1
            x += 1


class GameBoard:

    def __init__(self, lawn):
        self.game_board = lawn
        self.zombie_die = []

    def __str__(self):
        return f'{self.game_board}'

    def __repr__(self):
        return str(self)

    def arrange_plants_on_the_board(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[0])):
                if (c := self.game_board[i][j]) not in [' ', 'S']:
                    self.game_board[i][j] = Plant(int(c), i, j)
                elif c == 'S':
                    self.game_board[i][j] = PlantS(1, i, j)


def plants_and_zombies(lawn, zombies: list):
    all_zombies = [Zombie(s, r, h) for s, r, h in zombies]
    # Board the game
    board = GameBoard(get_game_board(lawn))
    board.arrange_plants_on_the_board()

    game_progress = 0
    flag_game = False
    zombies_on_board = []

    while True:
        # Exit game
        # Win plants
        if len(board.zombie_die) == len(zombies):
            return None
        # Win zombie
        if flag_game:
            return game_progress

        # Removing dead zombies from the board
        zombies_on_board = list(set(zombies_on_board) - set(board.zombie_die))
        # Removing exposed zombies from the board
        all_zombies = list(set(all_zombies) - set(zombies_on_board))
        # Sort the zombies in order from left to right from top to bottom
        zombies_on_board = list(sorted(zombies_on_board, key=lambda x: x.row and x.col))

        # Step up zombie
        if zombies_on_board:
            for zombie in zombies_on_board:
                zombie.step_up(board)
                if zombie.col == 0:
                    flag_game = True
                # kill plant
                if type(board.game_board[zombie.row][zombie.col]) == Plant:
                    board.game_board[zombie.row][zombie.col] = ' '
                elif type(board.game_board[zombie.row][zombie.col]) == PlantS:
                    board.game_board[zombie.row][zombie.col] = ' '

        # The appearance of zombies on the board
        for zombie in all_zombies:
            if zombie not in zombies_on_board:
                if zombie.step == game_progress:
                    zombie.step_on_board(board)
                    zombies_on_board.append(zombie)

        # Shoot the simple plant
        for row in range(len(board.game_board)):
            for col in range(len(board.game_board[0])):
                if type(board.game_board[row][col]) == Plant:
                    board.game_board[row][col].shoot(board)
        # Shoot the plant "S"
        for row in range(len(board.game_board)):
            for col in range(len(board.game_board[0]) - 1, -1, -1):
                if type(board.game_board[row][col]) == PlantS:
                    board.game_board[row][col].shoot(board)
                    board.game_board[row][col].shoot_diagonal_top(board)
                    board.game_board[row][col].shoot_diagonal_down(board)

        print(f'game_progress: {game_progress}')
        print(f'print_board(board) после выстрела:')
        print_board(board)
        game_progress += 1


def print_board(board: GameBoard):
    for item in board.game_board:
        print(item)


def get_game_board(board: list[str]):
    game_board = []
    for item in board:
        game_board.append(list(item))

    return game_board


# print(plants_and_zombies(
#     [
#         '12      ',
#         '2S      ',
#         '1S      ',
#         '2S      ',
#         '3       '],
#     [[0, 0, 15], [1, 1, 18], [2, 2, 14], [3, 3, 15], [4, 4, 13], [5, 0, 12], [6, 1, 19], [7, 2, 11], [8, 3, 17],
#      [9, 4, 18], [10, 0, 15], [11, 4, 14]]))
# print(plants_and_zombies(['41S        ',
#                           ' 22        ',
#                           '2S1S       ',
#                           '2S 11      ',
#                           '3SS        ',
#                           'S5 11      ',
#                           ' S1 3      '],
#                          [[0, 0, 29], [0, 3, 24], [0, 4, 24], [0, 6, 24], [1, 0, 19], [1, 3, 16], [1, 4, 16],
#                           [1, 5, 43], [2, 1, 23], [2, 2, 29], [2, 5, 27], [2, 6, 18], [3, 2, 18], [3, 3, 13],
#                           [3, 4, 13], [4, 0, 18], [4, 1, 16], [4, 2, 12], [4, 5, 22], [4, 6, 14], [5, 1, 11],
#                           [6, 3, 14], [8, 4, 16], [8, 6, 15], [9, 0, 21], [9, 1, 11], [9, 5, 27], [10, 6, 13],
#                           [12, 2, 20], [12, 3, 17], [12, 4, 16], [13, 0, 20], [14, 1, 13], [14, 2, 16], [14, 3, 13],
#                           [14, 4, 13], [14, 5, 29]]))
print(plants_and_zombies([' S31    ',
                          'SS4     ',
                          '33      ',
                          'S11     ',
                          '2SS5    ',
                          '31S2    ',
                          '3122    ',
                          '21S1    '],
                         [[0, 2, 21], [0, 3, 10], [0, 4, 32], [0, 5, 25], [0, 6, 28], [1, 0, 20], [1, 1, 24],
                          [1, 2, 14], [1, 3, 7],
                          [1, 4, 22], [1, 5, 17], [1, 6, 19], [1, 7, 20], [2, 0, 13], [2, 2, 11], [2, 3, 5],
                          [2, 6, 14], [2, 7, 13], [3, 0, 9], [3, 5, 15], [3, 7, 9], [5, 1, 21], [5, 2, 11], [5, 3, 6],
                          [5, 4, 24], [5, 6, 15],
                          [6, 0, 10], [6, 1, 14], [6, 4, 17], [6, 5, 15], [6, 7, 10], [7, 3, 6], [7, 6, 16],
                          [8, 1, 13], [8, 2, 14], [8, 5, 14], [8, 7, 10], [9, 0, 12], [9, 2, 11], [9, 3, 6],
                          [9, 6, 16], [10, 1, 13], [10, 4, 26], [11, 0, 11], [11, 2, 11], [11, 3, 6], [11, 4, 18],
                          [11, 6, 16], [11, 7, 12], [12, 1, 13], [12, 5, 21]]))
