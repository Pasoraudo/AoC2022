def allDiferentChar(data, long, i):
    return long == len(set(data[i:i+long]))
    
with open('./AoCdata/day6.txt', 'r') as f:
    data = f.read()
long1, long2 = 4, 14
prob1 = 0
while prob1 < len(data) - long1 and not allDiferentChar(data, long1, prob1):
    prob1 += 1
prob1 += long1
print('Problema 1: ', prob1)
prob2 = 0
while prob2 < len(data) - long2 and not allDiferentChar(data, long2, prob2):
    prob2 += 1
prob2 += long2
print('Problema 2: ', prob2)

