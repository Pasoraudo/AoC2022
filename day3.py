with open('./AoCdata/2022/day3.txt', 'r') as f:
    data = f.read().split('\n')
res1 = 0
for pack in data:
    lP = int(len(pack) / 2)
    letra = set(pack[:lP]) & set(pack[lP:])
    letra = letra.pop()
    res1 += ord(letra) - ord('a') + 1 if letra.islower() else ord(letra) - ord('A') + 27 
print('Problema 1', res1)

i = 0
res2 = 0
while i < len(data):
    letra = set(data[i]) & set(data[i+1]) & set(data[i+2])
    letra = letra.pop()
    res2 += ord(letra) - ord('a') + 1 if letra.islower() else ord(letra) - ord('A') + 27 
    i += 3
print('Problema 2', res2)
