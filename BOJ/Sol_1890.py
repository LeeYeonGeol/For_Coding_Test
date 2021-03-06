n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# dp 테이블 설정
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

# 이동 설정
dx = [1,0]
dy = [0,1]

# 답 계산 및 출력
for x in range(n):
    for y in range(n):
        if x == n-1 and y == n-1:
            break
        for i in range(2):
            nx = x + dx[i]*arr[x][y]
            ny = y + dy[i]*arr[x][y]
            if 0 <= nx < n and 0 <= ny < n:
                dp[nx][ny] += dp[x][y]
print(dp[n-1][n-1])