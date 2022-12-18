import numpy as np
import matplotlib.pyplot as plt


with open('./data/day18.txt', 'r') as f:
    data = f.read().split('\n')
data = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in data]

coor = [((0,0,0), (1,0,0)),
        ((0,0,0), (0,1,0)),
        ((0,0,0), (0,0,1)),
        ((0,0,1), (1,0,1)),
        ((0,0,1), (0,1,1)),
        ((1,0,0), (1,1,0)),
        ((0,1,0), (1,1,0)),
        ((1,0,1), (1,1,1)),
        ((0,1,1), (1,1,1)),
        ((0,1,0), (0,1,1)),
        ((1,0,0), (1,0,1)),
        ((1,1,0), (1,1,1))
         ]
aristas = []
for x, y, z in data:
    for p1, p2 in coor:
        a = set([(x + p1[0], y + p1[1], z+p1[2]), (x + p2[0], y + p2[1], z+p2[2])])
        aristas.append(a)
aux = {}
n = 0
for a in aristas:
    a = tuple(a)
    if a not in aux:
        aux[a] = 1
    else:
        aux[a] += 1
for i, j, v in aux:
    print(k, v)
    if v == 1:
        n += 1     
print(n)
mapa = np.zeros((7,7,7))
for x, y, z in data:
    mapa[x, y, z] = 1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for x, y, z in data:
    ax.scatter(x, y, z, marker='x')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
