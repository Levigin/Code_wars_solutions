import heapq
import math
import numpy as np


# the main method --> A-star covering 366 36 98 989
def find_shortest_path(grid, start_node, end_node):
    # border case:
    if len(grid) == 0 or len(grid[0]) == 0:
        return []

    def choose_heuristic():
        def calc_manhattan_heuristic(node_1, node_2):
            return abs(node_1.position.x - node_2.position.x) + abs(node_1.position.y - node_2.position.y)

        def calc_euclidian_heuristic(node_1, node_2):
            return math.sqrt(
                (node_1.position.x - node_2.position.x) ** 2 + (node_1.position.y - node_2.position.y) ** 2)

        def calc_no_heuristic(node_1, node_2):
            return 0

        heuristics = {1: calc_manhattan_heuristic, 2: calc_euclidian_heuristic, 3: calc_no_heuristic}
        heur_names = ['Manhattan', 'Euclidian', 'No']

        for i in range(len(heur_names)):
            print(f'press {i + 1} for <{heur_names[i]} heuristic>')

        string = input()
        if string in [str(_ + 1) for _ in range(len(heur_names))]:
            print(f'{heur_names[(i := int(string)) - 1]} heuristic been chosen')
            return heuristics[i]
        else:
            print('Please, press 1, 2, or 3 for heuristic choice')
            choose_heuristic()

    heuristic = choose_heuristic()

    print(f'start_node: {start_node}, end_node: {end_node}')
    print(f'grid: {grid}')

    path = a_star(grid, start_node, end_node, heuristic)
    print(f"The shortest path's length: {len(path)}")

    return [node.position for node in path]


def a_star(grid, start_node, end_node, heuristic):
    vertexes_to_be_visited = [start_node]
    start_node.g = 0

    heapq.heapify(vertexes_to_be_visited)

    iterations = 0

    while len(vertexes_to_be_visited) > 0:
        curr_node = heapq.heappop(vertexes_to_be_visited)
        # just a number of a-star iterations needed for building the shortest path from starting node to the ending one
        iterations += 1
        print(f'curr node x, y: ({curr_node.position.x}, {curr_node.position.y}), iteration: {iterations}')

        # stop condition, here we reach the ending point
        if curr_node == end_node:
            print(f'The path is done in {iterations} iterations')
            break

        # here we're looking for all the adjacent and passable nodes for a current node and pushing them to the heap (priority queue)
        for next_possible_node in get_adjacent_ones(grid, curr_node):
            if not next_possible_node.is_visited:
                if next_possible_node.g > curr_node.g + 1:  # a kind of dynamic programming
                    next_possible_node.g = curr_node.g + 1  # every step distance from one node to an adjacent one is equal to 1
                    next_possible_node.h = heuristic(next_possible_node, end_node)  # heuristic function,
                    # needed for sorting the nodes to be visited in priority order
                    next_possible_node.is_visited = True  # this node has just been visited
                    next_possible_node.previously_visited_node = curr_node  # constructing the path
                    heapq.heappush(vertexes_to_be_visited, next_possible_node)  # adding node to the heap

    # the last point of the path found
    node = end_node
    print(f'node: {node.position}')
    reversed_shortest_path = []

    # path restoring (here we get the reversed path)
    while node.previously_visited_node:
        reversed_shortest_path.append(node)
        node = node.previously_visited_node

    reversed_shortest_path.append(start_node)

    print(f'reversed_shortest_path: {reversed_shortest_path}')

    # returning the right shortest path
    return list(reversed(reversed_shortest_path))


# looks for all the adjacent and passable nodes
def get_adjacent_ones(grid, node):
    list_of_adj_nodes = []

    x, y = node.position.x, node.position.y

    if x > 0 and (n := grid[y][x - 1]).passable:
        list_of_adj_nodes.append(n)

    if x < len(grid[0]) - 1 and (n := grid[y][x + 1]).passable:
        list_of_adj_nodes.append(n)

    if y > 0 and (n := grid[y - 1][x]).passable:
        list_of_adj_nodes.append(n)

    if y < len(grid) - 1 and (n := grid[y + 1][x]).passable:
        list_of_adj_nodes.append(n)

    return list_of_adj_nodes


# not needed for the time being
def is_position_valid():
    pass


# simple class for Node's coordinate pair representation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x},{self.y})'


# class, describing the node's signature
class Node:

    def __init__(self, x, y, passability=True):
        self.position = Point(x, y)  # (2,5)
        self.passable = passability  # says if a cell is a wall or a path
        self.is_visited = False  # flag of visiting the current node
        self.previously_visited_node = None  # for building the shortest path of Nodes from the starting point to the ending one

        self.g = np.Infinity  # aggregated cost of moving from start to the current Node, Infinity chosen for convenience and algorithm's logic
        self.h = 0  # approximated cost evaluated by heuristic for path starting from the current node and ending at the exit Node
        # f = h + g or total cost of the current Node is not needed here

    def __eq__(self, other):
        return self.position == other.position

    # this is needed for using Node objects in priority queue like heapq and so on
    def __lt__(self, other):
        return self.h + self.g < other.h + other.g  # the right sigh is "-" for __lt__() method


# converts a grid of nodes from codewars to a convenient grid of Nodes, using extended Node-class
def convert_grid(grid, start_node, end_node):
    converted_grid = [[Node(i, j, grid[i][j].passable) for j in range(len(grid))] for i in range(len(grid[0]))]
    converted_start_node, converted_end_node = converted_grid[start_node.position.x][start_node.position.y], \
                                               converted_grid[end_node.position.x][end_node.position.y]

    return converted_grid, converted_start_node, converted_end_node


# converts the shortest path found to the list of initial nodes from the grid given
def convert_path_back(grid, path):
    return [grid[point.x][point.y] for point in path]


# creates a testing grid
def create_grid():
    # just a shaped grid with all passable nodes
    grid = [[Node(i, j) for j in range(8)] for i in range(11)]

    # generating obstacles
    grid[1][0].passable = False
    grid[1][1].passable = False
    grid[1][2].passable = False
    grid[2][2].passable = False
    grid[3][2].passable = False
    grid[3][0].passable = False
    grid[4][0].passable = False
    grid[5][0].passable = False
    grid[5][1].passable = False
    grid[5][2].passable = False
    grid[5][3].passable = False
    grid[5][4].passable = False
    grid[5][5].passable = False
    grid[3][4].passable = False
    grid[2][4].passable = False
    grid[1][4].passable = False
    grid[1][5].passable = False
    grid[1][6].passable = False
    grid[2][6].passable = False
    grid[3][6].passable = False
    grid[4][7].passable = False
    grid[5][7].passable = False
    grid[6][7].passable = False
    grid[7][7].passable = False
    grid[7][6].passable = False
    grid[7][5].passable = False
    grid[7][4].passable = False
    # grid[8][4].passable = False
    grid[7][0].passable = False
    grid[7][1].passable = False
    grid[9][1].passable = False
    grid[9][2].passable = False
    grid[9][3].passable = False
    grid[9][6].passable = False
    grid[10][5].passable = False

    print(f'grid been built')

    return grid


# makes a grid from a blueprint given
def make_grid_from_blueprint(blueprint: str):
    enters_q = blueprint.count('\n')
    length = len(blueprint)

    x_max, y_max = (length - 1) // (enters_q - 1) - 1, enters_q - 1

    grid = [[Node(i, j) for i in range(x_max)] for j in range(y_max)]

    for y in range(y_max):
        for x in range(x_max):
            iterator = y * (x_max + 1) + x + 1
            if (ch := blueprint[iterator]) == '0':
                grid[y][x] = Node(x, y)
            elif ch == '1':
                grid[y][x] = Node(x, y, False)
            elif ch == 'S':
                starting_node = grid[y][x] = Node(x, y)
            elif ch == 'E':
                ending_node = grid[y][x] = Node(x, y)

    print(f'starting point: {starting_node.position}, ending one: {ending_node.position}')

    return grid, starting_node, ending_node


blueprint_little = """
S0110
01000
01010
00010
0001E
"""