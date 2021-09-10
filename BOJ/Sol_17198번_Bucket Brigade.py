from collections import deque

graph = []

x, y = 0, 0

for k in range(10):
    sub = list(input())
    graph.append(sub)
    for p in range(10):
        if sub[p] == 'B':
            x, y = k, p

visited = [[False]*10 for _ in range(10)]

q = deque()
q.append((x, y, 0))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited[x][y] = True

while q:
    nx, ny, level = q.popleft()


    if graph[nx][ny] == 'L':
        print(level-1)
        break

    for k in range(4):
        nnx = nx + dx[k]
        nny = ny + dy[k]
        if 0 <= nnx < 10 and 0 <= nny < 10 and visited[nnx][nny] == False and graph[nnx][nny] != 'R':
            visited[nnx][nny] = True
            q.append((nnx, nny, level+1))