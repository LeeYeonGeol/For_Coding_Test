from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 앞은 sword가 없는 경우, 뒤는 있는 경우
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]

q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = int(1e9)

# x, y, cnt
q.append((0, 0))
visited[0][0][0] = 0

while q:

    x, y  = q.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            for p in range(2):
                if visited[x][y][p] == -1:
                    continue
                if p == 0 and visited[nx][ny][p] == -1:
                    if graph[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny][p] = visited[x][y][p]+1
                    elif graph[nx][ny] == 2:
                        q.append((nx, ny))
                        visited[nx][ny][p+1] = visited[x][y][p]+1
                elif p == 1 and visited[nx][ny][p] == -1:
                    q.append((nx, ny))
                    visited[nx][ny][p] = visited[x][y][p]+1

answer = int(1e9)
for f in range(2):
    if visited[n-1][m-1][f] != -1:
        answer = min(answer, visited[n-1][m-1][f])

if answer == int(1e9) or answer > t:
    print("Fail")
else:
    print(answer)
