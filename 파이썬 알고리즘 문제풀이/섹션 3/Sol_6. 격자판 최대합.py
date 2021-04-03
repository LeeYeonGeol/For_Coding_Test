n = int(input())

arr = []
ans = 0
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 각 행의 합 # 각 열의 합
sum1 = sum2 = 0

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    ans = max(ans, sum1)
    ans = max(ans, sum2)


# 대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-1-i]

ans = max(ans, sum1)
ans = max(ans, sum2)

print(ans)




