from random import randint

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import AStarFinder


class Hq:
    def __init__(self, file):
        self.y, self.x, self.reward = map(int, file.readline().split())

    def __str__(self):
        return "%s:%s, %s" % (self.x, self.y, self.reward)


def path_to_string(path):
    x, y = path[0]
    out = str(x) + ' ' + str(y) + ' '
    for k in range(len(path) - 2):
        x1, y1 = path[k]
        x2, y2 = path[k + 1]
        if x1 > x2:
            out += "L"
        elif x1 < x2:
            out += "R"
        elif y1 > y2:
            out += "U"
        elif y1 < y2:
            out += "D"
    print(out)


def get_path_cost(path, mappa):
    cost = 0
    for k in path:
        x, y = k
        cost += mappa[y][x]
    return cost


def pick_closest(start, ends):
    path = []
    cost = 1000000000000
    index = 0
    for i in range(len(ends)):
        new_path, runs = finder.find_path(start, ends[i], grid)
        # print('path length:', len(new_path), ', path_cost: ', cost)
        grid.cleanup()
        new_cost = get_path_cost(new_path, mappa)
        if new_cost < cost:
            path = new_path
            cost = new_cost
            index = i
    # print(grid.grid_str(path=path, start=start, end=ends[index]))
    if len(path) > 0:
        ends.remove(ends[index])
    return path


def pick_start_points():
    arr = []
    for _ in range(r):
        arr.append(grid.node(*punti[randint(0, len(punti) - 1)]))
    return arr


in_file = open("1_victoria_lake.txt", "r")

# N: width of map
# M: height of map
# C: number of Headquarters
# R: maximum number of Offices
n, m, c, r = map(int, in_file.readline().split())
hqs = []
for _ in range(c):
    hqs.append(Hq(in_file))

costs = {
    '#': 0,  # Non-walkable cell
    '\n': 0,  # a capo
    '~': 800,  # Water
    '*': 200,  # Traffic jam
    '+': 150,  # Dirt
    'X': 120,  # Railway level crossing
    '_': 100,  # Standard terrain
    'H': 70,  # Highway
    'T': 50,  # Railway
}

mappa = []
for i in range(n):
    row = []
    for j in range(m + 1):
        row.append(costs[in_file.read(1)])
    mappa.append(row)

punti = []
for i in range(n):
    for j in range(m + 1):
        if mappa[i][j] != 800 and mappa[i][j] != 0:
            punti.append((i, j))

for i in range(len(hqs) - 1):
    mappa[hqs[i].x][hqs[i].y] = 0

grid = Grid(matrix=mappa)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

paths = []
ends = []
for i in range(len(hqs)):
    ends.append(grid.node(hqs[i].x, hqs[i].y))

starts = pick_start_points()
out = []
for k in range(len(hqs)):
    p = pick_closest(starts[k % r], ends)
    if len(p) > 0:
        path_to_string(p)
