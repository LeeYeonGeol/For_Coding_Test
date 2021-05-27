n = int(input())

dp = [1,1,1]

for i in range(n-1):
    dp[0], dp[1], dp[2] = sum(dp), dp[0]+dp[2], dp[0]+dp[1]

print(sum(dp)%9901)


