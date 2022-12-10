import numpy as np
with open('./AoCdata/day8.txt', 'r') as f:
    data = f.read().split('\n')
data = np.array([list(map(int, line)) for line in data])
X, Y = np.shape(data)
num_visible_trees = 2 * X + 2*(Y - 2)
best_dist = -1
i = 1
while i < X - 1:
    j = 1
    while j < Y - 1:
        act_tree = data[i, j]
        left = np.flip(data[i,:j])
        right = data[i, j+1:]
        up = np.flip(data[:i,j])
        down = data[i+1:, j]
        if (act_tree > np.max(left) or act_tree > np.max(right) or
         act_tree > np.max(up) or act_tree > np.max(down)): 
            num_visible_trees += 1
        dist = 1
        for line in [right, left, up, down]:
            aux = np.where(line >= act_tree)[0]
            k = aux[0] + 1 if len(aux) > 0 else len(line)
            dist *= k
        if dist > best_dist:
            best_dist = dist
        j += 1
    i += 1
print('Problema 1:', num_visible_trees)
print('Problema 2:', best_dist)
        
