n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = [[2]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni <= n-1 and 0 <= nj <= m-1:
                if arr[ni][nj] > arr[i][j]:
                    ans[i][j] += (arr[ni][nj] - arr[i][j])
            else:
                ans[i][j] += arr[i][j]

res = 0
for a in ans:
    res += sum(a)
print(res)