from heapq import heappop, heappush, _heapify_max
import time


def voraz(plano, time):
    ore_robot_cost = plano[0]
    clay_robot_cost = plano[1]
    obsidian_robot_cost = plano[2]
    geode_robot_cost = plano[3]
    s = (time, 1, 0, 0, 0, 0, 0, 0, 0)
    for i in range(time):
        (time, ore_robot, clay_robot, 
        obsidian_robot, geode_robot,
        ore, clay, obsidian, geodas) = s

        aux = (time - 1, ore_robot, clay_robot, obsidian_robot, geode_robot, 
            ore + ore_robot, clay + clay_robot, 
            obsidian + obsidian_robot, geodas + geode_robot)
        if ore >= geode_robot_cost[0] and obsidian >= geode_robot_cost[1]:
            aux = (time - 1, ore_robot, clay_robot, obsidian_robot, geode_robot + 1, 
                ore + ore_robot - geode_robot_cost[0], clay + clay_robot, 
                obsidian + obsidian_robot - geode_robot_cost[1], geodas + geode_robot)
        elif ore >= obsidian_robot_cost[0] and clay >= obsidian_robot_cost[1]:
            aux = (time - 1, ore_robot, clay_robot, obsidian_robot + 1, geode_robot, 
                ore + ore_robot - obsidian_robot_cost[0], clay + clay_robot - obsidian_robot_cost[1], 
                obsidian + obsidian_robot, geodas + geode_robot)
        elif ore >= clay_robot_cost:
            aux = (time - 1, ore_robot, clay_robot + 1, obsidian_robot, geode_robot, 
            ore + ore_robot - clay_robot_cost, clay + clay_robot, 
            obsidian + obsidian_robot, geodas + geode_robot)
        elif ore >= ore_robot_cost:
            aux = (time - 1, ore_robot + 1, clay_robot, obsidian_robot, geode_robot, 
            ore + ore_robot - ore_robot_cost , clay + clay_robot, 
            obsidian + obsidian_robot, geodas + geode_robot)
        s = aux
    return s[-1]

def branches(s, plano):
    ore_robot_cost = plano[0]
    clay_robot_cost = plano[1]
    obsidian_robot_cost = plano[2]
    geode_robot_cost = plano[3]
    (time, 
    ore_robot, clay_robot, obsidian_robot, geode_robot,
    ore, clay, obsidian, geodas) = s
    res = []

    aux = (time - 1, ore_robot, clay_robot, obsidian_robot, geode_robot, 
            ore + ore_robot, clay + clay_robot, 
            obsidian + obsidian_robot, geodas + geode_robot)
    res.append(aux)
    if ore >= ore_robot_cost:
        aux = (time - 1, ore_robot + 1, clay_robot, obsidian_robot, geode_robot, 
        ore + ore_robot - ore_robot_cost , clay + clay_robot, 
        obsidian + obsidian_robot, geodas + geode_robot)
        res.append(aux)
    if ore >= clay_robot_cost:
        aux = (time - 1, ore_robot, clay_robot + 1, obsidian_robot, geode_robot, 
        ore + ore_robot - clay_robot_cost, clay + clay_robot, 
        obsidian + obsidian_robot, geodas + geode_robot)
        res.append(aux)
    if ore >= obsidian_robot_cost[0] and clay >= obsidian_robot_cost[1]:
        aux = (time - 1, ore_robot, clay_robot, obsidian_robot + 1, geode_robot, 
            ore + ore_robot - obsidian_robot_cost[0], clay + clay_robot - obsidian_robot_cost[1], 
            obsidian + obsidian_robot, geodas + geode_robot)
        res.append(aux)
    if ore >= geode_robot_cost[0] and obsidian >= geode_robot_cost[1]:
        aux = (time - 1, ore_robot, clay_robot, obsidian_robot, geode_robot + 1, 
            ore + ore_robot - geode_robot_cost[0], clay + clay_robot, 
            obsidian + obsidian_robot - geode_robot_cost[1], geodas + geode_robot)
        res.append(aux)
    return res

"""
    Para la cota optimista se tenemos infinita cantidad de ore:
    - ore -> math.inf
"""
def cota_optimista(s, plano): 
    obsidian_robot_cost = plano[2]
    geode_robot_cost = plano[3]
    (time, 
    ore_robot, clay_robot, obsidian_robot, geode_robot,
    ore, clay, obsidian, geodas) = s

    clay_robot_opt = clay_robot
    obsidian_robot_opt = obsidian_robot
    geode_robot_opt = geode_robot

    for i in range(time):
        # Comenzar a crear de robots
        obsidian_robot_opt_creados = 0
        if clay >= obsidian_robot_cost[1]:
            obsidian_robot_opt_creados = 1
            clay -= obsidian_robot_cost[1]
        geode_robot_opt_creados = 0
        if obsidian >= geode_robot_cost[1]:
            geode_robot_opt_creados = 1
            obsidian -= geode_robot_cost[1]

        #Generación de recursos
        clay += clay_robot_opt
        obsidian += obsidian_robot_opt
        geodas += geode_robot_opt

        # Robots ya contruidos
        clay_robot_opt += 1 # Esto no se si está bien
        obsidian_robot_opt += obsidian_robot_opt_creados
        geode_robot_opt += geode_robot_opt_creados
    return geodas

        

def solve(plano, time):
    s = (time, 1, 0, 0, 0, 0, 0, 0, 0)
    geodas_max = voraz(plano, time)
    cota = cota_optimista(s, plano)

    A = [(cota, s)]
    _heapify_max(A)
    while len(A) > 0:
        cota, s = heappop(A)
        (time, ore_robot, clay_robot, 
        obsidian_robot, geode_robot,
        ore, clay, obsidian, geodas) = s
        if cota < geodas:
            break
        for hijo in branches(s, plano):
            if hijo[0] <= 0:
                if hijo[0] == 0 and hijo[-1] > geodas_max:
                    geodas_max = hijo[-1]
            else:
                cota = cota_optimista(hijo, plano)
                if cota > geodas_max:
                    heappush(A, (cota, hijo))
    return geodas_max


with open('./AoCdata/2022/day19.txt', 'r') as f:
    data = f.read().split('\n')

blueprints = [] 
for line in data:
    aux = line.split(' ')
    blueprint_num = int(aux[1][:-1])
    ore_robot = int(aux[6])
    clay_robot = int(aux[12])
    obsidian_robot = (int(aux[18]), int(aux[21]))
    geode_robot = (int(aux[27]), int(aux[30]))
    blueprints.append([ore_robot, clay_robot, obsidian_robot, geode_robot])

quality_level = 0

for i, plano in enumerate(blueprints):
    geodes = solve(plano, 24)
    quality_level +=  (i + 1) * geodes

print('Problema 1:', quality_level)

geodes2 = []
for plano in blueprints[:3]:
    geodes2.append(solve(plano, 32))
print('Problema 2:', geodes2[0] * geodes2[1] * geodes2[2])
    