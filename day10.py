import math
with open('./AoCdata/2022/day10.txt', 'r') as f:
    instructions = f.read().split('\n')
cycle = 0
strength = 0
register = 1
line = ''
def cathode_ray():
    global cycle
    global strength
    global register
    global line
    npixel = cycle % 40
    pixel = '#' if register - 1 <= npixel <= register + 1 else '.'
    cycle += 1
    line += pixel
    if not cycle % 40:
        print(line)
        line = ''
    if not (cycle - 20) % 40:
        strength += cycle * register
for i in instructions:
    if 'addx' in i:
        for j in range(2):
            cathode_ray()
        register += int(i[4:])
    else:
        cathode_ray()
if (cycle - 20) % 40 == 0:
    strength += cycle * register
print(('-'*40))
print(('-')*int((38 - len(str(strength))) / 2), strength, ('-')*int((39 - len(str(strength))) / 2))
print(('-'*40))



        
