import math


class Hq:
    def __init__(self, file):
        self.x, self.y, self.reward = file.readline().split()


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
    '#': math.inf,  # Non-walkable cell
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
    for j in range(m):
        row.append(in_file.read(1))
    mappa.append(row)
