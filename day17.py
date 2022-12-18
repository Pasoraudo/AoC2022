import math
import numpy as np

def choca(rock):
    for x, y in rock:
        if mapa[x, y] == 1:
            return True
    return False

with open('./data/day17.txt', 'r') as f:
    jets = f.read()

min_x, max_x = 0, 6
rock1 = ((0, 0), (1, 0), (2, 0), (3, 0) )
rock2 = ((0, 1), (1, 0), (1, 2), (2, 1))
rock3 = ((0, 0), (1, 0), (2,0), (2,1), (2,2))
rock4 = ((0,0), (0,1), (0,2), (0,3))
rock5 = ((0,0), (1,0), (0,1), (1,1))
rocks = [ rock1, rock2, rock3, rock4, rock5 ]

max_y = 40000000
mapa = np.zeros((7, max_y))
for x in range(7):
    mapa[x, 0] = 1
h_torre = 0
n_jet = 0
i = 0
h_max_ant = 0
h_submapa = 0
n = 0
submapa = np.zeros((7, 100))
submapa_ant = np.ones((7, 100))
while i < 1000000:
    rock = rocks[i % len(rocks)]
    rock = [(x + 2, y + h_torre + 4) for x, y in rock]
    aux = rock
    n += 1
    while not choca(aux):
        if n_jet == 0:
            print(submapa_ant)
            print(submapa)
            print()
            if np.all(submapa == submapa_ant):
                print((2022 - i) / 7 * h_submapa + h_max_ant)
            h_max_ant = h_torre
            submapa_ant = np.copy(submapa)
            submapa = np.zeros((7, 100))
            n = 0
        jet = jets[n_jet]
        n_jet = (n_jet + 1) % len(jets)  
        # Desplazar en X
        if jet == '>':
            aux = [(x + 1, y) for x, y in rock]
            if max(aux)[0] <= 6 and not choca(aux):
                rock = aux
        else:
            aux = [(x - 1, y) for x, y in rock]
            if min(aux)[0] >= 0 and not choca(aux):
                rock = aux
        #Desplazar en y
        aux = [(x, y-1) for x, y in rock]
        if not choca(aux):
            rock = aux
    
    if max(rock[-1][1], rock[-2][1]) + 1 > h_torre:
        h_torre = max(rock[-1][1], rock[-2][1])
        h_submapa = h_torre - h_max_ant
    for x, y in rock:
        mapa[x, y] = 1
        submapa[x, y-h_max_ant] = 1
    i += 1
print(h_torre)