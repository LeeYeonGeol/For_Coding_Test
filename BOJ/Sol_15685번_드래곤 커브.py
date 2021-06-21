import copy

n = int(input())

ans = [[0]*101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    x, y = y, x
    go = [d]

    # -> 위 <- 아래
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]


    # 세대에 따라 진행
    for i in range(g):
        if i == 0:
            go.append((d+1)%4)
        else:
            ngo = copy.deepcopy(go)
            ngo = ngo[::-1]
            for n in ngo:

                go.append((n+1)%4)

    ans[x][y] = 1
    for g in go:
        x, y = x+dx[g], y+dy[g]
        ans[x][y] = 1

res = 0

for i in range(100):
    for j in range(100):
        if ans[i][j] + ans[i+1][j] + ans[i][j+1] + ans[i+1][j+1] == 4:
            res += 1
print(res)