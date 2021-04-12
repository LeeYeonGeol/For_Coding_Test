import collections

graph = []

for _ in range(7):
    graph.append(list(map(int, input().split())))

ans = [[0 for _ in range(7)] for _ in range(7)]

q = collections.deque()

q.append((0,0))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
            continue
        if ans[nx][ny] == 0 and graph[nx][ny] == 0:
            ans[nx][ny] = ans[x][y]+1
            q.append((nx,ny))

if ans[6][6] == 0:
    print(-1)
else:
    print(ans[6][6])
