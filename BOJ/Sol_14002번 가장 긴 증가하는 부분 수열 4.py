n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n
v = [-1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
            v[i] = j


ans = max(dp)
print(ans)

p = [i for i, x in enumerate(dp) if x == ans][0]

def dfs(p):
    if p == -1:
        return
    dfs(v[p])
    print(arr[p], end=' ')

dfs(p)
print()





