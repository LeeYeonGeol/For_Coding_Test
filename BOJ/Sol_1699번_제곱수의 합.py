n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    j = 1
    while(1):
        if i - (j*j) < 0:
            break

        dp[i] = min(dp[i], dp[i - (j*j)]+1)
        j += 1

print(dp[n])