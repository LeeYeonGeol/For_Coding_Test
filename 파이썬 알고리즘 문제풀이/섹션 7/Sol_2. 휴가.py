n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0

def dfs(time, csum):
    global ans
    if time > n:
        return
    ans = max(ans, csum)

    for i in range(time, n):
        dfs(i+arr[i][0], csum+arr[i][1])


for i in range(n):
    dfs(i, 0)

print(ans)

