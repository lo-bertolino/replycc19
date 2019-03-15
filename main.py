import math


class Hq:
    def __init__(self, file):
        self.y, self.x, self.reward = map(int, file.readline().split())

    def __str__(self):
        return "%s:%s, %s" % (self.x, self.y, self.reward)


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
    '\n': math.inf,  # a capo
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

for i in range(len(hqs) - 1, 0, -1):
    reachable = False
    for y in range(hqs[i].y - 1, hqs[i].y + 1, 2):
        if 0 <= y < n and mappa[y][hqs[i].x] != math.inf:
            reachable = True
    for x in range(hqs[i].x - 1, hqs[i].x + 1, 2):
        if 0 <= x < m and mappa[hqs[i].y][x] != math.inf:
            reachable = True
    if not reachable:
        hqs.remove(hqs[i])
        continue
    else:
        mappa[hqs[i].x][hqs[i].y] = -hqs[i].reward
print(len(hqs))
for i in range(n):
    print(mappa[i])

