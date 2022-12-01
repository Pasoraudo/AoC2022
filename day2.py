with open('./data/day1.txt', 'r') as f:
    data = f.read().split('\n\n')
calories = []
for line in data:
    num = sum([int(i) for i in line.split()])
    calories.append(num)
calories = sorted(calories, reverse=True)
print('Problema 1: ', calories[0])
print('Problema 2: ', sum(calories[:3]))