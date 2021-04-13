import itertools
n, m = map(int, input().split())

graph = []

house = []
pizza = []
for i in range(n):
    sub = list(map(int, input().split()))
    graph.append(sub)
    for j in range(n):
        if sub[j] == 2:
            pizza.append((i, j))
        elif sub[j] == 1:
            house.append((i, j))

ans = int(1e9)
for k in list(itertools.combinations(pizza,m)):
    dis = 0
    for h in house:
        sub = int(1e9)
        for b in k:
            sub = min(sub, abs(h[0]-b[0])+abs(h[1]-b[1]))
        dis += sub
    ans = min(ans, dis)
print(ans)
