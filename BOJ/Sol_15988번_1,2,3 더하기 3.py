dp = [0]*(1000001)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    dp[i] %= 1000000009

t = int(input())

for _ in range(t):
    print(dp[int(input())])
