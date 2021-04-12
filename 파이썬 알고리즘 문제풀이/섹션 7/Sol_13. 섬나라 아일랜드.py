import collections

n = int(input())


ans1 = 0

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def bfs(a, b):
    q = collections.deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            ans1 += 1
            bfs(i, j)

print(ans1)

