def rps1(a, b):
    if a == b:
        return 3 + b
    elif a % 3 + 1 == b:
        return 6 + b
    return b
    
def rps2(a, b):
    if b == 1: #loss
        return (a + 1) % 3 + 1
    elif b == 2: #tie
        return a + 3
    return 6 + a % 3 + 1 #win
    
d = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
with open('./data/day2.txt', 'r') as f:
    data = f.read().split('\n')
data = [(d[i.split()[0]], d[i.split()[1]]) for i in data]
prob1 = 0
for i in data:
    prob1 += rps1(i[0], i[1])
prob2 = 0
for i in data:
    prob2 += rps2(i[0], i[1])
print('Problema 1', prob1)
print('Problema 2', prob2)
