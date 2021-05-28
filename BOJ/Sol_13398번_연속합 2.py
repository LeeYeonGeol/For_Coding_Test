import copy
n = int(input())

arr = list(map(int, input().split()))

dp1 = copy.deepcopy(arr)
dp2 = copy.deepcopy(arr)

for i in range(n):
    if i == 0:
        continue
    dp1[i] = max(arr[i], dp1[i-1]+arr[i])

for i in range(n-1, -1, -1):
    if i == n-1:
        continue
    dp2[i] = max(arr[i], dp2[i+1]+arr[i])

ans = max(dp1)

for i in range(1, n-1):
    ans = max((dp1[i-1]+dp2[i+1]), ans)

print(ans)