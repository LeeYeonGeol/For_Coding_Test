n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

dp = [[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i-1]
    dp[i][2] = dp[i-1][1] + arr[i-1]

print(max(dp[n]))