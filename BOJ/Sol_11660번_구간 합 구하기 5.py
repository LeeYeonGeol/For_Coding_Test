import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for a in range(n):
    sub = list(map(int, input().split()))
    graph.append(sub)
    for b in range(n):
        if a == 0 and b == 0:
            continue
        elif a == 0:
            graph[a][b] += graph[a][b-1]
        elif b == 0:
            graph[a][b] += graph[a-1][b]
        else:
            graph[a][b] += graph[a][b-1]
            graph[a][b] += graph[a-1][b]
            graph[a][b] -= graph[a-1][b-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    ans += graph[x2-1][y2-1]
    if x1-2 >= 0:
        ans -= graph[x1-2][y2-1]
    if y1-2 >= 0:
        ans -= graph[x2-1][y1-2]
    if x1-2 >= 0 and y1-2 >= 0:
        ans += graph[x1-2][y1-2]

    print(ans)