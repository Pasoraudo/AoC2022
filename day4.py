with open('./AoCdata/2022/day4.txt', 'r') as f:
    data = f.read().split()
res = 0
res2 = 0
for i in data:
    a = i.split(',')[0]
    b = i.split(',')[1]
    af = a.find('-')
    bf = b.find('-')
    a = set(range(int(a[:af]), int(a[af+1:])+1))
    b = set(range(int(b[:bf]), int(b[bf+1:])+1))
    if a.union(b) == a or a.union(b) == b:
        res += 1
    if bool(a & b):
        res2 += 1
print(res)
print(res2)