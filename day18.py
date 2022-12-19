from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

with open('./data/day18.txt', 'r') as f:
    data = f.read().split('\n')
data = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in data]
caras_aux = [
        ((0,0,0), (1,0,0), (1,1,0), (0,1,0)),
        ((0,0,0), (1,0,0), (1,0,1), (0,0,1)),
        ((0,0,0), (0,0,1), (0,1,1), (0,1,0)),
        ((0,1,0), (0,1,1), (1,1,1), (1,1,0)),
        ((1,0,0), (1,0,1), (1,1,1), (1,1,0)),
        ((0,0,1), (1,0,1), (1,1,1), (0,1,1))
        ]
caras = []
for x, y, z in data:
    for p1, p2, p3, p4 in caras_aux:
        aux = set([
                (x + p1[0], y + p1[1], z+p1[2]), 
                (x + p2[0], y + p2[1], z+p2[2]),
                (x + p3[0], y + p3[1], z+p3[2]),
                (x + p4[0], y + p4[1], z+p4[2])
                ])
        caras.append(aux)

seen = []
eje_x, eje_y, eje_z = {}, {}, {}
res2 = {}
res = 0
for cara in caras:
    if cara not in seen:
        seen.append(cara)
        aux = list(cara)
        x1, y1, z1 = aux[0]
        x2, y2, z2 = aux[1]
        x3, y3, z3 = aux[2]
        x4, y4, z4 = aux[3]
        p_min = aux[0]
        for i in aux[1:]:
            if i[0] + i[1] + i[2] < p_min[0] + p_min[1] + p_min[2]:
                p_min = i
        if x1 == x2 == x3 == x4:
            eje_x[(p_min[1], p_min[2])] = 1
        elif y1 == y2 == y3 == y4:
            eje_y[(p_min[0], p_min[2])] = 1
        else:
            eje_z[(p_min[0], p_min[1])] = 1
        res += 1
    else:
        res -= 1
r=0
sub = [(1,0,0), (0,1,0), (0,0,1), (-1, 0,0), (0,-1,0), (0,0,-1)]
for x, y, z in data:
    for i, j, k in sub:
        if (x+i, y+j, z+k) not in data:
            r += 1
    print(r)
print(r)
# 1672 es demaasiado bajo
print('Problema 1:', res)
print((len(eje_x) + len(eje_y)+len(eje_z))*2)
print("hola chavalitos del youtube vamos baked as fuck")
