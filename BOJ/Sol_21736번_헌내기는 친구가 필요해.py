from collections import deque

n, m = map(int, input().split())

campus = []

nx, ny = -1, -1
for x in range(n):
    sub = list(input())
    for y in range(m):
        if sub[y] == 'I':
            nx, ny = x, y
    campus.append(sub)

ans = 0

visited = [[False]*m for _ in range(n)]

# 탐색 시작
q = deque()
q.append((nx, ny))
visited[nx][ny] = True

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    nx, ny = q.popleft()

    for k in range(4):
        nnx = nx + dx[k]
        nny = ny + dy[k]
        if 0 <= nnx < n and 0 <= nny < m and visited[nnx][nny] == False:
            visited[nnx][nny] = True

            # 벽인 경우 못지나감
            if campus[nnx][nny] == 'X':
                continue
            if campus[nnx][nny] == 'P':
                ans += 1
            q.append((nnx, nny))

if ans == 0:
    print("TT")
else:
    print(ans)







