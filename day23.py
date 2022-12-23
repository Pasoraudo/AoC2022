import numpy as np

with open('./AoCdata/2022/day23.txt', 'r') as f:
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

def alone(elf): # elf -> (x, y) coordenadas
    x, y = elf
    is_alone = True
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j == 0:
                is_alone = is_alone and mapa[x+i, y+j] == 0
    return is_alone

def propose(elfs, mapa, directions):
    for x, y in elfs:
        if not alone((x, y)):
            for d in directions:
                d_x, d_y = d
                [mapa[x+i, y+j] for i in range(-d_x, d_x+1) for j in range(-d_y, d_y+1)] #north
