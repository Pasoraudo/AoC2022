with open('./AoCdata/day1.txt', 'r') as f:
    data = f.read().split('\n\n')
data = [list(map(int, line.split())) for line in data]
calories = sorted(list(map(sum, data)), reverse=True)
print('Problema 1: ', calories[0])
print('Problema 2: ', sum(calories[:3]))