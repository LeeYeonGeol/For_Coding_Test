n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

ans = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def cal_max(x, y):
    ans = 1
    arr = graph[x]
    cnt1 = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            cnt1 += 1
        else:
            cnt1 = 1
        ans = max(ans, cnt1)

    arr = []
    for i in range(n):
        arr.append(graph[i][y])

    cnt2 = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            cnt2 += 1
        else:
            cnt2 = 1
        ans = max(ans, cnt2)

    return ans
for x in range(n):
    for y in range(n):
        # 위아래로 비교
        nx, ny = x+1, y
        if 0 <= nx < n and 0 <= ny < n:
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            ans = max(ans, cal_max(x, y))
            ans = max(ans, cal_max(nx, ny))
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
        # 옆으로 비교
        nx, ny = x, y+1
        if 0 <= nx < n and 0 <= ny < n:

            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]

            ans = max(ans, cal_max(x, y))
            ans = max(ans, cal_max(nx, ny))
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]

print(ans)