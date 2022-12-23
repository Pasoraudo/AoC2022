import math


with open('./AoCdata/2022/day12.txt', 'r') as f:
    data = f.read().split('\n')

def find(a):
    for x, line in enumerate(data):
        for y, e in enumerate(line):
            if e == a:
                return (x, y)
    return None

def val(pos):
    a = data[pos[0]][pos[1]]
    if a == 'S':
        return ord('a')
    elif a == 'E':
        return ord('z')
    return ord(a)

def is_promissing(l, p):
    ant_pos = l[-2]
    new_pos = l[-1]
    if len(l) > best_steps:
        return False
    if new_pos in caminos and len(caminos[new_pos]) < len(l)+1:
        return False
    if not (0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0])):
        return False
    if p == 1:
        return val(new_pos) - 1 <= val(ant_pos)
    else:
        return val(ant_pos) - 1 <= val(new_pos)

def is_complete(l, a):
    return data[l[-1][0]][l[-1][1]] == a

def prob(pos, end, p):
    global best_steps
    global caminos
    pila = [pos]
    while len(pila) > 0:
        pos = pila.pop(-1)
        l = caminos[pos]
        if is_complete(l, end):
            if len(l) <= best_steps:
                best_steps = len(l) - 1
        incrementos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in incrementos:
            new_pos = (pos[0] + i[0], pos[1] + i[1])
            l.append(new_pos)
            if is_promissing(l, p):
                pila.append(new_pos)
                caminos[new_pos] = l.copy()
            l.pop(-1)
    return best_steps

best_steps = math.inf
caminos = {}
pos = find('S')
caminos[pos] = [pos]
print(prob(pos, 'E', 1))

caminos = {}
pos = find('E')
caminos[pos] = [pos]
print(prob(pos, 'a', 2))

