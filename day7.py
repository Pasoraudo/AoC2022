with open('./data/day7.txt', 'r') as f:
    data = f.read().split('\n')
i = 1
directories = {'/': 0}
dir_act = '/'
def prob1(dir_act):
    global i
    global directories
    global data
    res = 0
    while i < len(data):
        line = data[i]
        if line.split()[0].isdigit():
            res += int(line.split()[0])
        elif 'cd' in line:
            if '..' in line:
                directories[dir_act] += res
                return res
            else:
                i += 1
                aux = dir_act + line[5:] + '/'
                if aux not in directories:
                    directories[aux] = 0
                res += prob1(aux)
        i += 1
    directories[dir_act] += res
    return res
while i < len(data):    
    directories[dir_act] += prob1('/')
dir_sizes = list(directories.values())
disk_size = 70000000
update_size = 30000000
unasigned_space = disk_size - directories['/']
min_dir = disk_size
for i in dir_sizes:
    aux = i + unasigned_space
    if aux > update_size and aux < min_dir + unasigned_space:
        min_dir = i
print('Problema 1:', sum([i if i <= 100000 else 0 for i in dir_sizes]))
print('Problema 2:', min_dir)
    
