from sympy.solvers import solve
from sympy import Symbol


def prob1(monkeys, monkeys_waiting):
    while type(monkeys['root']) != int:
        aux = []
        for monkey in monkeys_waiting:
            n1, n2 = monkeys[monkey][1], monkeys[monkey][2]
            if type(n1) != int and type(monkeys[n1]) == int:
                monkeys[monkey][1] = monkeys[n1]
            if type(n2) != int and type(monkeys[n2]) == int:
                monkeys[monkey][2] = monkeys[n2]
            n1, n2 = monkeys[monkey][1], monkeys[monkey][2]
            if type(n1) == int and type(n2) == int:
                op = monkeys[monkey][0]
                if op == '+':
                    res = n1 + n2
                elif op == '-':
                    res = n1 - n2
                elif op == '*':
                    res = n1 * n2
                elif op == '/':
                    res = int(n1 / n2) # supongo que todas las divisiones son enteras
                monkeys[monkey] = res
            else:
                aux.append(monkey)
        monkeys_waiting = aux
    return monkeys['root']

def operar(e1, e2, op):
    if op == '+':
        res = e1 + e2
    elif op == '-':
        res = e1 - e2
    elif op == '*':
        res = e1 * e2
    elif op == '/':
        res = int(e1 / e2)
    return res

def calculadora_polaca_str(operacion):
    operadores = ('+', '-', '*', '/')
    pila = []
    for e in operacion:
        print(pila, e)
        if e in operadores:
            pila.append(e)
        else:
            if not pila[-1] in operadores:
                e1, e2, op = pila.pop(), e, pila.pop()
                pila.append('(' + e1 + op + e2 + ')')
            else:
                pila.append(e)
    print(pila)
    return pila[0]

"""def calculadora_polaca(operacion):
    operadores = ('+', '-', '*', '/')
    pila = []
    for e in operacion:
        if e in operadores:
            pila.append(e)
        else:
            if pila[-1].isdigit():
                e1, e2, op = pila.pop(), e, pila.pop()
                pila.append(e1, e2, op)
            else:
                pila.append(e)
    return pila"""

def prob2(monkeys):
    operadores = ('+', '-', '*', '/')
    monkeys['humn'] = ['x']
    print(monkeys['root'])
    ecuaciones = []
    for r in monkeys['root'][1:]:
        operacion = [r]
        i = 0
        while i < len(operacion):
            e = operacion[i]
            if e in operadores:
                continue
            if type(monkeys[e]) == list:
                operacion = operacion[:i] + monkeys[e] + operacion[i+1:]
            else:
                operacion[i] = monkeys[e]
            i += 1
        print(operacion, 'op')
        ecuaciones.append(calculadora_polaca_str(operacion))
    print(ecuaciones)
    return calculadora_polaca_str(operacion)   

with open('./data/day21.txt', 'r') as f:
    data = f.read().split('\n')
monkeys = {}
monkeys_waiting = []
for line in data:
    l = line.split(':')
    name = l[0]
    ec = l[1][1:].split(' ')
    if len(ec) > 1:
        monkeys[name] = [ec[1], ec[0], ec[2]]
        monkeys_waiting.append(name)
    else:
        monkeys[name] = ec[0]
#print('Problema 1:', prob1(monkeys.copy(), monkeys_waiting.copy()))
print('Problema 2:', prob2(monkeys))


