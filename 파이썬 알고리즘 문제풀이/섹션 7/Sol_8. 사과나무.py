import collections

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

q = collections.deque()

q.append((n//2, n//2, 0))

visited[n//2][n//2] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
while q:
    #print(q)
    x, y, cnt = q.popleft()
    ans += graph[x][y]

    if cnt == n//2:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))
print(ans)
