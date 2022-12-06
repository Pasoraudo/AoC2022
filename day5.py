with open('./data/day5.txt', 'r') as f:
    data = f.read().split('\n\n')
crates = []
lista = data[0].split('\n')
lista.pop()
aux = data[0].split('\n')[-1]
for i in aux:
    if i == ' ':
        continue
    pos = int(i)
    x = aux.find(i)
    aux2 = []
    for j in lista:
        if j[x] != ' ':
            aux2.append(j[x])
    crates.append(aux2) 
steps = []
for i in data[1].split('\n'):
    aux = i.replace('move','').replace('from','').replace('to','').replace(' ','')
    steps.append((int(aux[:-2]), int(aux[-2]), int(aux[-1]))) 
crates2 = crates.copy()
for i in steps:
    #part 1
    blocks = crates[i[1] - 1][:i[0]]
    crates[i[1] - 1] = crates[i[1] - 1][i[0]:]
    crates[i[2] - 1] = list(reversed(blocks)) + crates[i[2] - 1]
    #part 2
    blocks2 = crates2[i[1] - 1][:i[0]]
    crates2[i[1] - 1] = crates2[i[1] - 1][i[0]:]
    crates2[i[2] - 1] = blocks + crates2[i[2] - 1]
print('Problema 1:', ''.join([i[0] if i != [] else '' for i in crates]))
print('Problema 2:', ''.join([i[0] if i != [] else '' for i in crates2]))