import math
import ast

with open('./data/day13.txt', 'r') as f:
    data1 = f.read().split('\n\n')
#data = [i.split('\n') for i in data]

def is_valid(izq, der):
    res = None
    i = 0
    while i < len(izq) and i < len(der) and res == None:
        e_izq = izq[i]
        e_der = der[i]
        if isinstance(e_izq, list) and isinstance(e_der, list):
            res = is_valid(e_izq, e_der)
        elif isinstance(e_izq, int) and isinstance(e_der, int):
            if e_izq != e_der:
                return e_izq < e_der
        elif isinstance(e_izq, int):
            res = is_valid([e_izq], e_der)
        elif isinstance(e_der, int):
            res = is_valid(e_izq, [e_der])
        else:
            print("Algo va mal")
        i += 1
    if res == None and (len(izq) != len(der)):
        return i == len(izq)
    return res
    
"""def converter(packet):
    list_ant = []
    list_act = list_ant
    res = list_ant
    i = 0
    while i < len(packet): 
        e = packet[i] 
        if e == '[':
            list_ant = list_act
            aux = []
            list_act.append(aux)
            list_act = aux
        elif e == ']':
            list_act = list_ant
        elif e.isdigit():
            if packet[i+1].isdigit():
                i += 1
                e = e + packet[i]
            list_act.append(int(e)) 
        i += 1
    return res[0]"""

"""res = 0    
for i, packet in enumerate(data):
    izq = ast.literal_eval(packet[0])
    der = ast.literal_eval(packet[1])
    if is_valid(izq, der):
        res += i + 1"""

def mergesort(m):
    left, right, result = [], [], []
    if len(m) <= 1:
        return m
    else:
        middle = int(len(m) / 2)
        left = m[:middle]
        right = m[middle:]
        left = mergesort(left)
        right = mergesort(right)
        if is_valid(left[-1],right[0]):
            left += right
            return left
        result = merge(left, right)
        return result

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if is_valid(left[0], right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0]) 
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

data = []
for packets in data1:
    for pack in packets.split('\n'):
        data.append(ast.literal_eval(pack))

data = mergesort(data)
for i, pack in enumerate(data):
    if pack == [[2]]:
        res = i + 1
    elif pack == [[6]]:
        res = res * (i + 1)
        break
print(res)

