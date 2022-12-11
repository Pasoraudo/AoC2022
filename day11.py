import math
from functools import partial


def mult(a, b):
    return a * b
def suma(a, b):
    return a + b
def pow(a):
    return a * a

with open('./AoCdata/day11.txt', 'r') as f:
    data = f.read().split('\n\n')
monkeys = []
mcm = 1
items_save = []
for monkey in data:
    m = monkey.split('\n')
    items = m[1].replace('Starting', '').replace('items:','').replace(' ','').replace(',', ' ')
    items = [int(i) for i in items.split()]
    operation = m[2].split()
    if operation[5] == 'old':
        operation = partial(pow)
    elif operation[4] == '+':    
        operation = partial(suma, int(operation[5]))
    else:
        operation = partial(mult, int(operation[5]))
    test = int(m[3].split()[3])
    mcm = int(mcm * test / math.gcd(mcm, test))
    result = (int(m[4].split()[5]), int(m[5].split()[5]))
    items_save.append(items.copy())
    monkeys.append({'items': items, 'op': operation, 'test': test, 'res': result})

item_count = [0 for i in range(len(monkeys))]
for m_round in range(20):
    for n, monkey in enumerate(monkeys):
        item_count[n] += len(monkey['items'])
        while len(monkey['items']) > 0:
            worry = monkey['items'].pop()
            worry = monkey['op'](worry)
            worry = int(worry / 3)
            if not (worry % monkey['test']):
                monkeys[monkey['res'][0]]['items'].append(worry)
            else:
                monkeys[monkey['res'][1]]['items'].append(worry)
item_count = sorted(item_count, reverse=True)  
prob1 = item_count[0] * item_count[1]

for i, monkey in enumerate(monkeys):
    monkey['items'] = items_save[i]
item_count = [0 for i in range(len(monkeys))]
for m_round in range(10000):
    for n, monkey in enumerate(monkeys):
        item_count[n] += len(monkey['items'])
        while len(monkey['items']) > 0:
            worry = monkey['items'].pop()
            worry = monkey['op'](worry)
            worry = worry % mcm
            if not (worry % monkey['test']):
                monkeys[monkey['res'][0]]['items'].append(worry)
            else:
                monkeys[monkey['res'][1]]['items'].append(worry)
item_count = sorted(item_count, reverse=True)  
prob2 = item_count[0] * item_count[1]

print('Problema 1:',  prob1)
print('Problema 2:',  prob2)





        
