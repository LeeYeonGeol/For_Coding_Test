graph = []

for _ in range(7):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(7)] for _ in range(7)]

visited[0][0] = True

ans = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x, y):
    global ans

    if x == 6 and y == 6:
        ans += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <= 6 and 0 <= ny <= 6 and visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False
dfs(0,0)
print(ans)