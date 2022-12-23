def desencriptar(code, data):
    for i, e in enumerate(data):
        index = code.index((i, e))
        if e == 0:
            save_0 = (i,e)
        code.pop(index)
        pos = (index + e) % (N-1)
        code = code[:pos] + [(i, e)] + code[pos:]
    return code, save_0


with open('./AoCdata/2022/day20.txt', 'r') as f:
    data = f.read().split('\n')
data = [int(e) for e in data]
code = [(i, e) for i, e in enumerate(data)]
N = len(data)
coor = [1000, 2000, 3000]
# Parte 1
res, save_0 = desencriptar(code.copy(), data)
pos_0 = res.index(save_0)
print('Problema 1:', sum(res[(i+pos_0)%N][1] for i in coor))
# Parte 2
description_key = 811589153
code = [(i, e * description_key) for i, e in code]
data = [i * description_key for i in data]
for i in range(10):
    code, save_0 = desencriptar(code, data)
pos_0 = code.index(save_0)
print('Problema 2:', sum(code[(i+pos_0)%N][1] for i in coor))

    