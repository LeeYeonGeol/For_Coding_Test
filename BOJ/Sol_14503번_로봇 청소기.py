graph = []
n, m = map(int,input().split())
x, y, d = map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))

# 0 = 북, 1 = 동, 2 = 남, 3 = 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 0
# 1. 현재 위치 청소
if graph[x][y] == 0:
    graph[x][y] = 2
    cnt += 1

turn_time = 0
while (1):
    # 2. 왼쪽 방향부터 차례대로 탐색 진행.
    turn_left()

    nx = x + dx[d]
    ny = y + dy[d]

    if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # c or d
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] != 1:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)
