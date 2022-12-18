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

def cota_optimista(flow, time, not_used):
    extra, i = 0, 0
    while i < len(not_used) and time <= 26:
        valvula = not_used[i]
        extra += flow_rates[valvula] * (26 - time)
        i += 1
        if i < len(not_used):
            extra += flow_rates[valvula] * (26 - time)
        time += 2
        i += 1
    return flow + extra

#esto no funciona porque el time del elephante no tiene porque ser el mismo que el mio
def solve(time, flow, not_used, ini):
    historial = []
    A = [(cota_optimista(flow, time, not_used), ini, ini, time, time, not_used, flow)]
    _heapify_max(A)
    historial.append((cota_optimista(flow, time, not_used), ini, ini, time, time, not_used, flow))
    x, fx = None, 1700 #1151  
    while len(A) != 0:
        cota_opt, val_act, elephant, time, time_elephant, not_used, flow = heappop(A)
        print(fx, cota_opt, val_act, elephant, time, time_elephant, not_used, flow)
        if cota_opt < fx:
            break
        for next_val in valvulas[val_act]:
            for next_elephant in valvulas[elephant]:
                if time >= 27 and time_elephant >= 27:
                    if time == 27 and time_elephant == 27 and flow > fx:
                        x, fx = (next_val, next_elephant, time, time_elephant, not_used, flow), flow
                        
                else:
                    if val_act in not_used and flow_rates[val_act] != 0:
                        i = not_used.index(val_act)
                        aux = not_used[:i] + not_used[i+1:]
                        val = flow_rates[val_act] * (26 - time)
                        cota = cota_optimista(flow, min(time, time_elephant) + 2, aux)
                        opt_next_val = cota + val
                        if opt_next_val > fx:
                            aux = (opt_next_val, 
                                    next_val, next_elephant, 
                                    time + 2, 
                                    time_elephant + 1,
                                    aux, 
                                    flow + val
                                )
                            if aux not in historial:
                                historial.append(aux)
                                heappush(A, aux)

                    if elephant in not_used and flow_rates[elephant] != 0:
                        i = not_used.index(elephant)
                        aux = not_used[:i] + not_used[i+1:]
                        val = flow_rates[elephant] * (26 - time_elephant)
                        cota = cota_optimista(flow, min(time_elephant, time) + 2, aux)
                        opt_next_val = cota + val
                        if opt_next_val > fx:
                            aux = (opt_next_val, 
                                    next_val, next_elephant, 
                                    time + 1, 
                                    time_elephant + 2,
                                    aux, 
                                    flow + val
                                )
                            if aux not in historial:
                                historial.append(aux)
                                heappush(A, aux)

                    if val_act != elephant and val_act in not_used and flow_rates[val_act] != 0:
                        i2 = not_used.index(val_act)
                        aux2 = not_used[:i2] + not_used[i2+1:]
                        val2 = flow_rates[val_act] * (26 - time)

                        if elephant in aux2 and flow_rates[elephant] != 0:
                            i = aux2.index(elephant)
                            aux = aux2[:i] + aux2[i+1:]
                            val = flow_rates[elephant] * (26 - time_elephant)

                            cota = cota_optimista(flow, min(time, time_elephant) + 2, aux)
                            opt_next_val = cota + val + val2
                            if opt_next_val > fx:
                                aux = (opt_next_val, 
                                        next_val, next_elephant, 
                                        time + 2, 
                                        time_elephant + 2,
                                        aux, 
                                        flow + val
                                    )
                                if aux not in historial:
                                    historial.append(aux)
                                    heappush(A, aux)

                    opt_next_val = cota_optimista(flow, min(time, time_elephant) + 1, not_used)
                    if opt_next_val > fx:
                        aux = (opt_next_val, next_val, next_elephant, time + 1, time_elephant+1,not_used, flow)
                        if aux not in historial:
                            historial.append(aux)
                            heappush(A, aux)
    return x, fx

orden = np.array(list(flow_rates.values()))
orden = np.argsort(orden)[::-1]
aux = list(valvulas.keys())
no_used_f = [aux[i] for i in orden]
#solve(30, 0, no_used, 'AA')
#print('voraz',voraz('AA'))
x, fx = solve(1, 0, no_used_f, 'AA')
print(x)
print(fx)
