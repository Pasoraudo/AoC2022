import math
from heapq import heappop, heappush, _heapify_max
import numpy as np

#1914 es más pequeño que el resultado
with open('./data/day16.txt', 'r') as f:
    data = f.read().split('\n')

res = {}
camino = {}
valvulas = {}
flow_rates = {}
for line in data:
    l2 = line.split(' ')
    valvulas[l2[1]] = [i.replace(',','') for i in l2[9:]]
    flow_rates[l2[1]] = int(l2[4][5:-1])

"""valvulasTiempo = [set(['AA'])]
for i in range(30):
    valvulasTiempo.append(set())
    for nodo in valvulasTiempo[i]:
        hijos = set(valvulas[nodo])
        valvulasTiempo[i+1] = valvulasTiempo[i+1].union(hijos)
print(valvulasTiempo) """
"""
def mas_prometedor(next_valvulas):
    if next_valvulas == []:
        return None
    next_valvulas = np.array(next_valvulas)
    flows = [flow_rates[next_val] for next_val in next_valvulas]
    indices = np.argsort(flows)[::-1]
    next_valvulas = next_valvulas[indices]
    return next_valvulas[0]

def voraz(ini):
    val_act = ini
    visitados = []
    time, flow = 1, 0
    while time <= 30 and val_act != None and val_act not in visitados:
        visitados.append(val_act)
        flow += flow_rates[val_act] * (30 - time)
        val_act = mas_prometedor([i for i in valvulas[val_act] if i not in visitados])
        time += 2
    return flow

def cota_optimista(flow, time, not_used):
    extra, i = 0, 0
    while i < len(not_used) and time <= 30:
        valvula = not_used[i]
        extra += flow_rates[valvula] * (30 - time)
        time += 2
        i += 1
    return flow + extra


def solve(time, flow, not_used, ini):
    historial = []
    A = [(cota_optimista(flow, time, not_used), ini, time, not_used, flow)]
    _heapify_max(A)
    historial.append((cota_optimista(flow, time, not_used), ini, time, not_used, flow))
    x, fx = None, 2262
    while len(A) != 0:
        cota_opt, val_act, time, not_used, flow = heappop(A)
        
        if cota_opt < fx:
            break
        for next_val in valvulas[val_act]:
            if time >= 31:
                if time == 31 and flow > fx:
                    x, fx = (next_val, time, not_used, flow), flow
                    print(fx, cota_opt, val_act, time, not_used, flow)
            else:
                if val_act in not_used and flow_rates[val_act] != 0:
                    i = not_used.index(val_act)
                    aux = not_used[:i] + not_used[i+1:]
                    val = flow_rates[val_act] * (30 - time)
                    cota = cota_optimista(flow, time + 2, aux)
                    opt_next_val = cota + val
                    if opt_next_val > fx:
                        aux = (opt_next_val, 
                                next_val, time + 2, 
                                 aux, 
                                 flow + val
                              )
                        if aux not in historial:
                            historial.append(aux)
                            heappush(A, aux)
                opt_next_val = cota_optimista(flow, time + 1, not_used)
                if opt_next_val > fx:
                    aux = (opt_next_val, next_val, time + 1, not_used, flow)
                    if aux not in historial:
                        historial.append(aux)
                        heappush(A, aux)
    return x, fx"""


def mas_prometedor(next_valvulas, elephant):
    if next_valvulas == []:
        return None
    next_valvulas = np.array(next_valvulas)
    flows = [flow_rates[next_val] for next_val in next_valvulas]
    indices = np.argsort(flows)[::-1]
    next_valvulas = next_valvulas[indices]
    return next_valvulas[0]

def voraz(ini):
    val_act = ini
    elephant = ini
    visitados = []
    time, flow = 1, 0
    while time <= 26 and val_act != None and val_act not in visitados:
        visitados.append(val_act)
        flow += flow_rates[val_act] * (26 - time)
        val_act = mas_prometedor([i for i in valvulas[val_act] if i not in visitados])
        time += 2
    return flow

def cota_optimista(s):
    flow, _, _, time, time_ele, _, not_used = s
    extra, i = 0, 0
    while i < len(not_used) and 1 < time and 1 < time_ele:
        yo = not_used[i]
        extra += flow_rates[yo] * time
        if i+1 < len(not_used):
            ele = not_used[i+1]
            extra += flow_rates[ele] * time_ele
        time -= 2
        time_ele -= 2
        i += 2
    print(extra, s)
    return flow + extra

def branches(s):
    flow, yo, ele, time, time_ele, act, not_used = s
    for yo_loc in valvulas[yo]:
        for ele_loc in valvulas[ele]:
            for yo_act in range(2):
                for ele_act in range(2):
                    act_aux = act.copy()
                    not_used_aux = not_used.copy()
                    if yo_act == ele_act == 1 and yo_loc == ele_loc:
                        continue
                    if time <= 1 or time_ele <= 1 and yo_act == ele_act == 1:
                        continue
                    if yo_act:
                        act_aux[yo_loc] = yo_act
                        not_used_aux.pop(not_used_aux.index(yo_loc))
                    if ele_act:
                        act_aux[ele_loc] = ele_act
                        not_used_aux.pop(not_used_aux.index(ele_loc))
                    aux = (flow + flow_rates[yo_loc] * yo_act * (time-1) + flow_rates[ele_loc] * ele_act * (time_ele-1),
                        yo_loc, ele_loc, time - 1 - yo_act, 
                        time_ele - 1 - ele_act, act_aux, not_used_aux)
                    yield aux

#esto no funciona porque el time del elephante no tiene porque ser el mismo que el mio
def solve(time):
    visited = {}
    not_used = []
    for k, v in flow_rates.items():
        not_used.append((v, k))
        visited[k] = 0
    not_used = [e for _, e in sorted(not_used, reverse=True)]
    s = (0, 'AA', 'AA', time, time, visited, not_used)
    A = [(cota_optimista(s), s)]
    _heapify_max(A)
    mejor_flow = 1151  #flow, yo, ele, my_time, ele_time, visitados
    while len(A) != 0:
        
        cota, s = heappop(A)
        flow, yo, ele, time, time_ele, act, not_used = s
        if cota < mejor_flow:
            break
        for hijo in branches(s):
            flow, yo, ele, time, time_ele, act, not_used = hijo
            #print(mejor_flow, hijo)
            if time <= 0 or time_ele <= 0:
                if time == time_ele == 0 and flow > mejor_flow:
                    
                    mejor_flow = flow
            if flow > mejor_flow:
                cota = cota_optimista(hijo)
                if cota > mejor_flow:
                    heappush(A, (cota, hijo))
    return mejor_flow
print(valvulas)
orden = np.array(list(flow_rates.values()))
orden = np.argsort(orden)[::-1]
aux = list(valvulas.keys())
fx = solve(26)
print(fx)
