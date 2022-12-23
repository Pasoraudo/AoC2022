import math
import ast
import numpy as np
with open('./AoCdata/2022/day14.txt', 'r') as f:
    data = f.read().split('\n')

def sand_flow(coor, mapa):
    stop = False
    x, y = coor
    while not stop:
        if y >= deepstY:
            return mapa, True
        if (x, y+1) not in mapa:
            y += 1
        elif (x - 1, y+1) not in mapa:
            x -= 1
            y += 1
        elif (x+1, y+1) not in mapa:
            x += 1
            y += 1
        else:
            mapa.append((x, y))
            stop = True
    #print((x,y))
    return mapa, False
    
def sand_flow2(coor, mapa):
    stop = False
    x, y = coor
    while not stop:
        if y == floor - 1:
            mapa[x, y] = 1
            stop = True
        elif mapa[x, y+1] == 0:
            y += 1
        elif mapa[x - 1, y+1] == 0:
            x -= 1
            y += 1
        elif mapa[x+1, y+1] == 0:
            x += 1
            y += 1
        else:
            mapa[x, y] = 1
            if (x, y) == center:
                return mapa, True
            stop = True
    #print((x, y))
    
    return mapa, False
mapa = []
deepstY, min_x, max_x = 0, math.inf, -math.inf
for inst in data:
    inst = inst.replace(' ','').split('->')
    i = 0
    while i < len(inst) - 1:
        inic = inst[i].split(',')
        final = inst[i+1].split(',')
        x1, x2 = min(int(inic[0]), int(final[0])), max(int(inic[0]), int(final[0]))
        y1, y2 = min(int(inic[1]), int(final[1])), max(int(inic[1]), int(final[1]))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if y > deepstY:
                    deepstY = y
                if min_x > x:
                    min_x = x
                if max_x < x:
                    max_x = x
                mapa.append((x,y))
        i += 1
floor = deepstY + 2
center = ((max_x - min_x), 0)
aux = np.zeros((max_x - min_x + 10000, deepstY + 2))
for x, y in mapa:
    aux[x-500+(max_x-min_x), y] = 1
print(aux)
in_void = False
"""res = 0
while not in_void:
    res += 1
    mapa, in_void = sand_flow((500, 0), mapa)
print(res-1)"""
deepstY = deepstY + 2
res = 0
while not in_void:
    res += 1
    #print(res)
    aux, in_void = sand_flow2(center, aux)
print(aux)
print(res)
