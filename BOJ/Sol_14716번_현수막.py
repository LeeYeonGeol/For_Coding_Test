from collections import deque

m, n = map(int, input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

ans = 0

for x in range(m):
    for y in range(n):
        if graph[x][y] == 1:
            ans += 1
            graph[x][y] = 0
            q = deque()
            q.append((x, y))

            while q:
                nx, ny = q.popleft()
                for k in range(8):
                    nnx = nx + dx[k]
                    nny = ny + dy[k]
                    if 0 <= nnx < m and 0 <= nny < n:
                        if graph[nnx][nny] == 1:
                            graph[nnx][nny] = 0
                            q.append((nnx, nny))


print(ans)