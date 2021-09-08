import sys
from collections import deque

n = int(input())

visited = [[False]* n for _ in range(n)]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


# 시작점
q = deque()

q.append((0, 0))
visited[0][0] = True

# bfs 시작
while q:
    x, y = q.popleft()
    n_distance = graph[x][y]

    if n_distance == -1:
        print("HaruHaru")
        sys.exit()

    sub = []

    # 좌표안의 경우만
    if 0<= x-n_distance:
        sub.append((x-n_distance, y))

    if x+n_distance < n:
        sub.append((x+n_distance, y))

    if 0<= y-n_distance:
        sub.append((x, y-n_distance))

    if y+n_distance < n:
        sub.append((x, y+n_distance))

    for nx, ny in sub:
        # 방문하지 않은 경우만
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))


print("Hing")