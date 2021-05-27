import copy
n = int(input())

arr = list(map(int, input().split()))

dp2 = copy.deepcopy(arr)

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i], dp2[j]+arr[i])

print(max(dp2))