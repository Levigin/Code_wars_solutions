import heapq as hq
import numpy as np


class Node:

    def __init__(self, y: int, x: int, height: int = 0):
        self.y, self.x = y, x
        self.g = np.Infinity
        self.h = 0
        self.previous_node = None
        self.height = height
        self.diff = 0

    def get_neighs(self, other: 'AStar'):
        neighs = []
        for step in other.directions:
            ny, nx = self.y + step[0], self.x + step[1]
            if 0 <= ny < len(other.grid_of_nodes) and 0 <= nx < len(other.grid_of_nodes):
                neighs.append(other.grid_of_nodes[ny][nx])
        return neighs

    def __str__(self):
        return f'{(self.y, self.x)}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.y == other.y) and (self.x == other.x)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h


class AStar:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, board: str):
        self.board_ = board.split('\n')
        size_ = len(self.board_)
        self.grid_of_nodes = [[Node(y, x) for x in range(size_)] for y in range(size_)]
        self.get_height()
        self.start = self.grid_of_nodes[0][0]
        self.end = self.grid_of_nodes[size_ - 1][size_ - 1]
        self.start.g = 0
        self.path_astar = [self.start]
        self.iterations = 0

    def get_height(self):
        for i in range(len(self.grid_of_nodes)):
            for j in range(len(self.grid_of_nodes)):
                self.grid_of_nodes[i][j].height = int(self.board_[i][j])

    def get_distance(self, node: Node) -> int:
        return abs(node.y - self.end.y) + abs(node.x - self.end.x)

    def a_star(self):
        hq.heapify(self.path_astar)
        while self.path_astar:
            self.iterations += 1
            curr_node = hq.heappop(self.path_astar)
            print(f'curr_node: {curr_node.g}')
            if curr_node == self.end:
                return curr_node.g

            for neigh in curr_node.get_neighs(self):
                print(f'neigh: {neigh.g}')
                if neigh.g > curr_node.g + abs(curr_node.height - neigh.height):
                    neigh.diff = abs(curr_node.height - neigh.height)
                    neigh.g = curr_node.g + neigh.diff
                    neigh.h = self.get_distance(neigh)
                    neigh.previous_node = curr_node
                    hq.heappush(self.path_astar, neigh)


def path_finder(area):
    astar = AStar(area)
    res = astar.a_star()
    return res


b = "\n".join([
    "6082999301",
    "2064977260",
    "4187212910",
    "7968457923",
    "2786036601",
    "2168765128",
    "0527919769",
    "1974111918",
    "3799265577",
    "7108744099"
])

f = "\n".join([
    "836",
    "264",
    "467"
])  # 9

e = "\n".join([
    "400001",
    "096729",
    "159828",
    "231368",
    "461818",
    "571882"
])  # 18

a = "\n".join([
    "3721516",
    "0220694",
    "6696027",
    "2309840",
    "1083729",
    "5219309",
    "4026251"
])

c = "\n".join(["08816959617",
               "75355377876",
               "99213808601",
               "54182721192",
               "85972763458",
               "52398577246",
               "19008423599",
               "49569552531",
               "08641712561",
               "27580534642",
               "91051583858"])  # 36

print(path_finder(f))

# astar = AStar(8, 7, Node(1, 1), Node(5, 5))
# astar.grid_of_nodes[5][1].possibility = False
# astar.grid_of_nodes[4][1].possibility = False
# astar.grid_of_nodes[3][1].possibility = False
# astar.grid_of_nodes[3][2].possibility = False
# astar.grid_of_nodes[3][3].possibility = False
# astar.grid_of_nodes[2][3].possibility = False
# astar.grid_of_nodes[1][3].possibility = False
# astar.grid_of_nodes[1][4].possibility = False
# astar.grid_of_nodes[1][5].possibility = False
# astar.a_star()

# astar = AStar(3, 3, Node(0, 0), Node(2, 2))
# astar.grid_of_nodes[0][1].height = 1
# astar.grid_of_nodes[0][0].height = 1
# astar.grid_of_nodes[1][1].height = 1
# astar.grid_of_nodes[2][1].height = 1
# astar.grid_of_nodes[2][2].height = 1
# astar.a_star()
