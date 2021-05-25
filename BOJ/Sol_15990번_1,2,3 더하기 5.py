# n = 계단 수
n = int(input())

# 1자리일 때 0~9 개수
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

# 값 계산및 출력
for i in range(2, n+1):

    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1]+ dp[i-1][j-1]

print(sum(dp[n])%1000000000)
