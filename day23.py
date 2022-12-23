import numpy as np

with open('./data/day23.txt', 'r') as f:
    data = f.read().split('\n')

N = 4000
elfs = []
mapa = np.zeros((N, N))
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == '#':
            print(i,j)
            elfs.append((i,j))
            mapa[i, j] = 1
print(mapa[:10, :10])
