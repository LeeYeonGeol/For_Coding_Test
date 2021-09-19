import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x, y = 0, 0

visited = [[False]*m for _ in range(n)]

visited[x][y] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

direction = 0
cnt = 1
while 1:
    if cnt == n*m:
        break
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            cnt += 1
            x, y = nx, ny
        else:
            direction += 1

    else:
        direction += 1

    direction %= 4


print(x, y)
