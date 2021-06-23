from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
coins = []

for i in range(n):
    c = list(input())
    graph.append(c)
    for j in range(m):
        if c[j] == "o":
            coins.append((i, j))

q = deque()

q.append((coins,0))

ans = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    coin, level = q.popleft()

    if ans < level:
        break

    # 10번 이상이면 break
    if level > 10:
        ans = min(ans, level)
        break

    # 4가지 버튼에 따라서
    for k in range(4):
        down = 0
        ncoin = []

        x, y = coin[0]
        xx, yy = coin[1]

        nx = x + dx[k]
        ny = y + dy[k]
        nxx = xx + dx[k]
        nyy = yy + dy[k]

        # 몇개 떨어지는지 조사
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            down += 1
        if nxx < 0 or nxx >= n or nyy < 0 or nyy >= m:
            down += 1

        if down == 0:
            if graph[nx][ny] == "#":
                nx, ny = x, y
            if graph[nxx][nyy] == "#":
                nxx, nyy = xx, yy

            q.append(([(nx, ny), (nxx, nyy)], level+1))
        elif down == 1:
            ans = min(ans, level+1)

if ans == int(1e9) or ans > 10:
    print(-1)
else:
    print(ans)