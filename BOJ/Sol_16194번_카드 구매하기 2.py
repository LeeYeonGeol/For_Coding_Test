n = int(input())

card = [0] + list(map(int,input().split()))

dp = [int(1e9)] * (n + 1)

dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i - j] + card[j])

print(dp[n])