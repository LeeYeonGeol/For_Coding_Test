n = int(input())

graph = []

ans1 = 0
ans2 = []

for _ in range(n):
    graph.append(list(map(int,input())))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        cnt = 0
        if graph[i][j] == 1:
            ans1 += 1
            dfs(i, j)
            ans2.append(cnt)

ans2.sort()

print(ans1)
for i in ans2:
    print(i)