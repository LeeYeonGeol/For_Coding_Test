import collections
n, m = map(int, input().split())

graph = []

q = collections.deque()

ans = 0

for i in range(m):
    sub = list(map(int, input().split()))
    graph.append(sub)
    for j in range(n):
        if sub[j] == 1:
            q.append((i,j,0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    for _ in range(len(q)):
        x, y, cnt = q.popleft()
        ans = cnt
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, cnt+1))

for i in graph:
    if 0 in i:
        ans = -1
        break

print(ans)


