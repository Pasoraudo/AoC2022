with open('./data/day5.txt', 'r') as f:
    data = f.read().split('\n\n')
cratesList = [] # lista de cratesList
lista = data[0].split('\n')
lista.pop()
aux = data[0].split('\n')[-1]
for i, j in enumerate(aux):
    if not j.isdigit():
        continue
    j = int(j)
    crates = []
    for j in lista:
        if j[i].isalpha():
            crates.append(j[i])
    cratesList.append(crates) 
steps = []
for i in data[1].split('\n'):
    aux = i.replace('move','').replace('from','').replace('to','').replace(' ','')
    steps.append((int(aux[:-2]), int(aux[-2]), int(aux[-1]))) 
cratesList2 = cratesList.copy()
for i in steps:
    #part 1
    blocks = cratesList[i[1] - 1][:i[0]]
    cratesList[i[1] - 1] = cratesList[i[1] - 1][i[0]:]
    cratesList[i[2] - 1] = list(reversed(blocks)) + cratesList[i[2] - 1]
    #part 2
    blocks2 = cratesList2[i[1] - 1][:i[0]]
    cratesList2[i[1] - 1] = cratesList2[i[1] - 1][i[0]:]
    cratesList2[i[2] - 1] = blocks + cratesList2[i[2] - 1]
print('Problema 1:', ''.join([i[0] if i != [] else '' for i in cratesList]))
print('Problema 2:', ''.join([i[0] if i != [] else '' for i in cratesList2]))