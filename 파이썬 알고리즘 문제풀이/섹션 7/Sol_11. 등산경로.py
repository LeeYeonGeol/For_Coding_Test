n = int(input())

graph = []

min_v = [int(1e9), 0, 0]
max_v = [-int(1e9), 0, 0]

ans = 0

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if min_v[0] > a[j]:
            min_v[0] = a[j]
            min_v[1], min_v[2] = i, j
        if max_v[0] < a[j]:
            max_v[0] = a[j]
            max_v[1], max_v[2] = i, j
    graph.append(a)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x, y):
    global ans
    if x == max_v[1] and y == max_v[2]:
        ans += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[x][y] < graph[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)
                    visited[nx][ny] = False

visited = [[False for _ in range(n)] for _ in range(n)]
visited[min_v[1]][min_v[2]] = True
dfs(min_v[1], min_v[2])

print(ans)