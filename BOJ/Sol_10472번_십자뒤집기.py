t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

place = []
for x in range(3):
    for y in range(3):
        place.append((x, y))

for _ in range(t):
    graph = []
    for _ in range(3):
        graph.append(list(input()))

    visited = [False]*9

    ans = 1e9

    change = dict()
    change['*'] = '.'
    change['.'] = '*'

    def dfs(level, now):
        global ans

        if level >= ans:
            return

        # 흰 보드인지 check하고 업데이트
        white = 0
        for k in range(3):
            white += graph[k].count('.')

        if white == 9:
            ans = level


        for k in range(now, 9):
            if visited[k] == False:
                visited[k] = True
                sub = []
                nx, ny = place[k]
                sub.append((nx, ny))
                for p in range(4):
                    nnx = nx + dx[p]
                    nny = ny + dy[p]
                    if 0 <= nnx < 3 and 0 <= nny < 3:
                        sub.append((nnx, nny))

                for s in sub:
                    xx, yy = s
                    graph[xx][yy] = change[graph[xx][yy]]
                dfs(level+1, k+1)
                visited[k] = False
                for s in sub:
                    xx, yy = s
                    graph[xx][yy] = change[graph[xx][yy]]

    dfs(0, 0)

    print(ans)



