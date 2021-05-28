n = int(input())

arr = list(map(int, input().split()))

dp1 = [1]*n
dp2 = [1]*n

# 바이토닉 기준
for k in range(n):
    for i in range(k):
        for j in range(i):
            if arr[j] < arr[i]:
                dp1[i] = max(dp1[i], dp1[j]+1)

    for i in range(n-1, k-1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j]+1)

dp3 = [0]*n

for i in range(n):
    dp3[i] = dp1[i] + dp2[i]
print(max(dp3)-1)