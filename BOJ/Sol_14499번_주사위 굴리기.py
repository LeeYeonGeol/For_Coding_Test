n, m, x, y, k = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

system = list(map(int, input().split()))

dice = [0]*7

now = [0,1,2,3,4,5,6]

direction = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]

for sys in system:
    xx, yy = direction[sys]
    nx, ny = x+xx, y+yy
    # 벗어나면 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 동, 서, 남, 북에 따라 ㅇㅇ
    if sys == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif sys == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif sys == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif sys == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[1]
    else:
        dice[1] = graph[nx][ny]
        graph[nx][ny] = 0

    print(dice[6])

    x = nx
    y = ny