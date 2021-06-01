from collections import deque
import sys

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]

ans = 1

q = deque()

q.append((0, 0))

visited = [[False] * m for _ in range(n)]

visited[0][0] = True

while q:
    nn = len(q)
    for _ in range(nn):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == n-1 and ny == m-1:
                print(ans+1)
                sys.exit()

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    ans += 1
