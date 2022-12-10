import math
with open('./AoCdata/day9.txt', 'r') as f:
    data = f.read().split('\n')
data = [(i[0], int(i[2:])) for i in data]
def rope_movements(rope):
    moves = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    directions = {(0, 2): [0, 1], (0, -2): [0, -1], (2, 0): [1, 0], (-2, 0): [-1, 0]}
    historial = []
    for step in data:
            direc = step[0]
            numSteps = step[1]
            for i in range(numSteps):
                rope[0][0] = rope[0][0] + moves[direc][0]
                rope[0][1] = rope[0][1] + moves[direc][1]
                i = 1
                while i < len(rope):
                    dif = (rope[i-1][0] - rope[i][0], rope[i-1][1] - rope[i][1])
                    if dif in directions:
                        rope[i][0] = rope[i][0] + directions[dif][0]
                        rope[i][1] = rope[i][1] + directions[dif][1]
                    elif math.pow(dif[0], 2) + math.pow(dif[1], 2) > 2:
                        rope[i][0] = rope[i][0] + sing(int(dif[0]))
                        rope[i][1] = rope[i][1] + int(dif[1] / abs(dif[1]))
                    i += 1
                if rope[-1] not in historial:
                    historial.append(rope[-1].copy())
    return len(historial)
print('Problema 1:', rope_movements( [[0,0] for i in range(2)] ))
print('Problema 2:', rope_movements( [[0,0] for i in range(10)] ))


        
